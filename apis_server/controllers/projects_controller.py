#
# Copyright (c) 2020-2021 Hopenly srl.
#
# This file is part of Ilyde.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import io
import mimetypes

import connexion
import etcd3
import six
from flask import current_app
from werkzeug.utils import secure_filename

from apis_server.decorators import catch_exception
from apis_server.serializers import ProjectRevisionSerializer, StatusSerializer, PageTokenListSerializer, \
    ModelSerializer, ModelVersionSerializer
from apis_server.serializers.project_serializer import ProjectSerializer
from apis_server import util, permissions
from apis_server.services import get_projects_services_stub, get_minio_client, get_datasets_services_stub, \
    get_experiments_services_stub, get_mlflow_client, get_runs_services_stub, get_workspaces_services_stub
from protos import project_pb2, dataset_pb2, job_pb2


def check_project_permission(obj, token_info):
    if not permissions.IsProjectMember.has_object_permission(token_info, obj):
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")


def get_project_object(project_id):
    stub = get_projects_services_stub()
    return stub.Retrieve(project_pb2.ID(id=project_id))


@catch_exception
def create_project(body, **kwargs):
    """Create a project
    :param body: Project object to be created
    :type body: dict | bytes

    :rtype: ProjectSerializer
    """
    stub = get_projects_services_stub()
    body["owner"] = kwargs["user"]
    response = stub.Create(project_pb2.Project(**body))

    return ProjectSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def create_project_revision(id_, **kwargs):
    """Create project's revision
    :param id_: The ID of the project resource
    :type id_: str

    :rtype: ProjectRevisionSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])
    # upload file in Minio
    files = connexion.request.files
    client = get_minio_client()
    # acquire lock to write
    etcd = etcd3.client(host=current_app.config.get("ETCD_HOST"),
                        port=current_app.config.get("ETCD_PORT"))
    # acquire lock
    commit_message = "Write"
    stub = get_projects_services_stub()

    with etcd.lock(proj.id, ttl=1800) as lock:
        for file in files.getlist('files'):
            filename = secure_filename(
                file.filename)  # This is convenient to validate your filename, otherwise just use file.filename

            file_type, _ = mimetypes.guess_type(filename)
            bio = io.BytesIO(file.read())
            client.put_object(data=bio,
                              bucket_name=proj.repo_bucket,
                              object_name=filename,
                              content_type=file_type,
                              length=len(bio.getvalue()))

            commit_message += " {}".format(filename)

        response = stub.CreateRevision(project_pb2.Revision(
            project=proj.id,
            commit=commit_message,
            author=kwargs["user"]
        ))

    return ProjectRevisionSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def delete_project(id_, **kwargs):
    """Delete a project
    :param id_: The ID of the project object to be deleted
    :type id_: str

    :rtype: StatusSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])
    stub = get_projects_services_stub()
    response = stub.Delete(project_pb2.ID(id=proj.id))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def list_project_datasets(id_, limit=None, page=None, **kwargs):
    """List project&#39;s datasets

    :param id_: The ID of the project resource
    :type id_: str
    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageLimitListSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    stub = get_datasets_services_stub()
    response = stub.SearchDatasets(dataset_pb2.SearchDatasetRequest(
        query={"project": proj.id, "scope": "Local"},
        limit=limit,
        page=page
    ))
    return util.deserialize_protobuf(response)


@catch_exception
def list_project_experiments(id_, limit=None, page=None, **kwargs):
    """Search for project's experiments

    :param id_: The ID of the project resource
    :type id_: str
    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageTokenListSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    stub = get_experiments_services_stub()
    response = stub.Search(job_pb2.SearchRequest(
        query={"project": proj.id},
        limit=limit,
        page=page
    ))
    return util.deserialize_protobuf(response)


@catch_exception
def list_project_models(id_, **kwargs):
    """List project's models
    :param id_: The ID of the project resource
    :type id_: str

    :rtype: PageTokenListSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    models = mlflow_client.list_registered_models(max_results=200)

    data = []
    for model in models:
        project_id = model.tags.get('ilyde.project', None)
        if project_id == proj.id:
            data.append(model)

    return PageTokenListSerializer(
        next_page_token=models.token,
        data=[ModelSerializer(
            name=model.name,
            description=model.description,
            tags=model.tags,
            latest_versions=[ModelVersionSerializer(
                creation_timestamp=version.creation_timestamp,
                current_stage=version.current_stage,
                description=version.description,
                last_updated_timestamp=version.last_updated_timestamp,
                name=version.name,
                run_id=version.run_id,
                source=version.source,
                status=version.status,
                status_message=version.status_message,
                tags=version.tags,
                version=version.version
            ) for version in model.latest_versions],
            last_updated_timestamp=model.last_updated_timestamp,
            creation_timestamp=model.creation_timestamp
        ) for model in data]
    )


@catch_exception
def list_project_revisions(id_, limit=None, page=None, **kwargs):
    """List project's revisions
    :param id_: The ID of the project resource
    :type id_: str
    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageLimitListSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    stub = get_projects_services_stub()
    response = stub.SearchRevision(project_pb2.SearchRevisionRequest(
        query={"project": proj.id},
        limit=limit,
        page=page
    ))

    return util.deserialize_protobuf(response)


@catch_exception
def list_project_runs(id_, limit=None, page=None, **kwargs):
    """List project's runs
    :param id_: The ID of the project resource
    :type id_: str
    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageTokenListSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    stub = get_runs_services_stub()
    response = stub.Search(job_pb2.SearchRequest(
        query={"project": proj.id},
        limit=limit,
        page=page
    ))
    return util.deserialize_protobuf(response)


@catch_exception
def list_project_workspaces(id_, limit=None, page=None, **kwargs):
    """List project's workspaces

    :param id_: The ID of the project resource
    :type id_: str
    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageTokenListSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    stub = get_workspaces_services_stub()
    response = stub.Search(job_pb2.SearchRequest(
        query={"project": proj.id},
        limit=limit,
        page=page
    ))
    return util.deserialize_protobuf(response)


@catch_exception
def list_projects(body=None, **kwargs):
    """List projects
    :param body:
    :type body: dict | bytes

    :rtype: PageLimitListSerializer
    """
    query = body.get("query")
    if not permissions.IsAdmin.has_permission(kwargs["token_info"]) and query["visibility"] == "PRIVATE":
        query["member"] = kwargs["user"]

    stub = get_projects_services_stub()
    response = stub.Search(project_pb2.SearchProjectRequest(
        query=query,
        limit=body.get("limit"),
        page=body.get("page")
    ))

    return util.deserialize_protobuf(response)


@catch_exception
def retrieve_project(id_, **kwargs):
    """Retrieve a project
    :param id_: The ID of the project object to be retrieved
    :type id_: str

    :rtype: ProjectSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    return ProjectSerializer.from_dict(util.deserialize_protobuf(proj))


@catch_exception
def update_project(id_, body, **kwargs):
    """Update a project
    :param id_: The ID of the project object to be updated
    :type id_: str
    :param body: Project object to be updated
    :type body: dict | bytes

    :rtype: ProjectSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])

    stub = get_projects_services_stub()
    proj.description = body["description"]
    response = stub.Update(proj)

    return ProjectSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def close_project(id_, **kwargs):
    """Close a project
    :param id_: The ID of the project object to be updated
    :type id_: str

    :rtype: ProjectSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])
    if proj.owner != kwargs["user"]:
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")
    proj.state = project_pb2.STATE.CLOSED
    stub = get_projects_services_stub()
    response = stub.Update(proj)

    return ProjectSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def add_project_member(id_, body, **kwargs):
    """Close a project
    :param id_: The ID of the project object to be updated
    :type id_: str
    :param body: User Id
    :type body: dict | bytes
    :rtype: ProjectSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])
    if proj.owner != kwargs["user"]:
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")

    if body["user"] not in proj.members:
        proj.members.append(body["user"])
        stub = get_projects_services_stub()
        proj = stub.Update(proj)

    return ProjectSerializer.from_dict(util.deserialize_protobuf(proj))


@catch_exception
def remove_project_member(id_, body, **kwargs):
    """Close a project
    :param id_: The ID of the project object to be updated
    :type id_: str
    :param body: User Id
    :type body: dict | bytes
    :rtype: ProjectSerializer
    """
    proj = get_project_object(id_)
    check_project_permission(proj, kwargs["token_info"])
    if proj.owner != kwargs["user"]:
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")

    if body["user"] in proj.members:
        proj.members.remove(body["user"])
        stub = get_projects_services_stub()
        proj = stub.Update(proj)

    return ProjectSerializer.from_dict(util.deserialize_protobuf(proj))
