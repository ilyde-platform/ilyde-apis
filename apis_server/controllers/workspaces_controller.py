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
import connexion
import six

from apis_server.decorators import catch_exception
from apis_server.serializers import StatusSerializer
from apis_server.serializers.workspace_serializer import WorkspaceSerializer
from apis_server import util, permissions
from apis_server.services import get_projects_services_stub, get_workspaces_services_stub, query_elasticsearch
from protos import project_pb2, job_pb2


def check_workspace_permission(obj, token_info):
    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=obj.metadata.project))
    if not permissions.IsProjectMember.has_object_permission(token_info, project):
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")


def get_workspace_object(workspace_id):
    stub = get_workspaces_services_stub()
    return stub.Retrieve(job_pb2.ID(id=workspace_id))


def get_latest_project_revision(project_id):
    stub = get_projects_services_stub()
    response = stub.SearchRevision(project_pb2.SearchRevisionRequest(
        query={"project": project_id},
        page=1,
        limit=5
    ))
    revision = response.data[0]
    return revision.id


@catch_exception
def create_workspace(body, **kwargs):
    """Create a workspace
    :param body: Workspace payload
    :type body: dict | bytes

    :rtype: WorkspaceSerializer
    """
    serializer = WorkspaceSerializer.from_dict(body)
    check_workspace_permission(serializer, kwargs["token_info"])

    stub = get_workspaces_services_stub()
    response = stub.Create(job_pb2.Workspace(**body))

    return WorkspaceSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def delete_workspace(id_, **kwargs):
    """Delete a workspace
    :param id_: The ID of the workspace resource
    :type id_: str

    :rtype: StatusSerializer
    """
    w = get_workspace_object(id_)
    check_workspace_permission(w, kwargs["token_info"])

    stub = get_workspaces_services_stub()
    response = stub.Delete(job_pb2.ID(id=id_))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def fetch_workspace_logs(id_, **kwargs):
    """Fetch logs of a given workspace.
    :param id_: The ID of the workspace resource
    :type id_: str

    :rtype: object
    """
    w = get_workspace_object(id_)
    check_workspace_permission(w, kwargs["token_info"])

    query = "ilyde-workspace-{}".format(w.id)
    return query_elasticsearch(query)


@catch_exception
def retrieve_workspace(id_, **kwargs):
    """Retrieve a workspace
    :param id_: The ID of the workspace resource
    :type id_: str

    :rtype: WorkspaceSerializer
    """
    w = get_workspace_object(id_)
    check_workspace_permission(w, kwargs["token_info"])

    return WorkspaceSerializer.from_dict(util.deserialize_protobuf(w))


@catch_exception
def start_workspace(id_, start_with_latest_version=False, **kwargs):
    """Start a job
    :param id_: The ID of the workspace resource
    :type id_: str
    :param start_with_latest_version: Start job with the latest revision of the project
    :type start_with_latest_version: bool

    :rtype: StatusSerializer
    """
    w = get_workspace_object(id_)
    check_workspace_permission(w, kwargs["token_info"])
    stub = get_workspaces_services_stub()

    if start_with_latest_version:
        w.spec.revision = get_latest_project_revision(w.metadata.project)
        w = stub.Update(w)

    response = stub.Start(job_pb2.ID(id=w.id))
    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def status_workspace(id_, **kwargs):
    """Get state of a workspace.
    :param id_: The ID of the workspace resource
    :type id_: str

    :rtype: Object
    """
    w = get_workspace_object(id_)
    check_workspace_permission(w, kwargs["token_info"])

    stub = get_workspaces_services_stub()
    response = stub.State(job_pb2.ID(id=id_))

    return util.deserialize_protobuf(response)


@catch_exception
def stop_workspace(id_, **kwargs):
    """Stop a running workspace.
    :param id_: The ID of the workspace resource
    :type id_: str

    :rtype: StatusSerializer
    """
    w = get_workspace_object(id_)
    check_workspace_permission(w, kwargs["token_info"])

    stub = get_workspaces_services_stub()
    response = stub.Stop(job_pb2.ID(id=id_))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))
