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
from werkzeug.utils import secure_filename

from apis_server.decorators import catch_exception
from apis_server.serializers.dataset_serializer import DatasetSerializer
from apis_server.serializers.dataset_version_serializer import DatasetVersionSerializer
from apis_server.serializers.error_serializer import ErrorSerializer
from apis_server.serializers.page_limit_list_serializer import PageLimitListSerializer
from apis_server.serializers.status_serializer import StatusSerializer
from apis_server import util, permissions
from apis_server.services import get_datasets_services_stub, get_projects_services_stub, get_minio_client
from protos import dataset_pb2, project_pb2


def check_dataset_permission(scope, project, token_info):
    if scope == "Local" and project:
        stub = get_projects_services_stub()
        project = stub.Retrieve(project_pb2.ID(id=project))
        if not permissions.IsProjectMember.has_object_permission(token_info, project):
            raise connexion.ProblemException(status=403, title="Permission Denied",
                                             detail="Doesn't have enough permissions to take this action")


@catch_exception
def create_dataset(body, **kwargs):
    """Create a dataset

    :param body: Dataset object to create
    :type body: dict | bytes
    :rtype: DatasetSerializer
    """
    if body["scope"] == "Local" and not body.get("project"):
        return ErrorSerializer(status=404,
                               title="Bad request",
                               detail="missing project for Local dataset."), 404

    check_dataset_permission(body.get("scope"), body.get("project"), kwargs["token_info"])

    stub = get_datasets_services_stub()
    dataset = stub.CreateDataset(dataset_pb2.Dataset(
        name=body["name"],
        description=body["description"],
        scope=body["scope"],
        project=body.get("project")
    ))

    return DatasetSerializer.from_dict(util.deserialize_protobuf(dataset))


@catch_exception
def create_dataset_version(id_, **kwargs):
    """Create dataset's version
    :param id_: The ID of the dataset resource
    :type id_: str
    :rtype: DatasetVersionSerializer
    """
    stub = get_datasets_services_stub()
    dataset = stub.RetrieveDataset(dataset_pb2.ID(id=id_))
    check_dataset_permission(dataset_pb2.SCOPE.Name(dataset.scope), dataset.project, kwargs["token_info"])

    bucket = stub.CreateBucket(dataset_pb2.Bucket())
    # upload file in Minio
    files = connexion.request.files
    client = get_minio_client()
    for file in files.getlist('files'):
        filename = secure_filename(
            file.filename)  # This is convenient to validate your filename, otherwise just use file.filename

        file_type, _ = mimetypes.guess_type(filename)
        bio = io.BytesIO(file.read())
        client.put_object(data=bio,
                          bucket_name=bucket.name,
                          object_name=filename,
                          content_type=file_type,
                          length=len(bio.getvalue()))

    # add dataset version
    request = dataset_pb2.Version(
        dataset=id_,
        related_bucket=bucket.name,
        author=kwargs["user"])

    version = stub.CreateVersion(request)
    return DatasetVersionSerializer.from_dict(util.deserialize_protobuf(version))


@catch_exception
def delete_dataset(id_, **kwargs):
    """Delete a dataset
    :param id_: The ID of the dataset resource
    :type id_ str

    :rtype: StatusSerializer
    """
    stub = get_datasets_services_stub()
    dataset = stub.RetrieveDataset(dataset_pb2.ID(id=id_))
    check_dataset_permission(dataset_pb2.SCOPE.Name(dataset.scope), dataset.project, kwargs["token_info"])

    response = stub.DeleteDataset(dataset_pb2.ID(id=id_))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def list_dataset_versions(id_, body=None, **kwargs):
    """Search for dataset's versions
    :param id_: The ID of the dataset resource
    :type id_: str
    :param body:
    :type body: dict | bytes

    :rtype: PageLimitListSerializer
    """

    stub = get_datasets_services_stub()
    dataset = stub.RetrieveDataset(dataset_pb2.ID(id=id_))
    check_dataset_permission(dataset_pb2.SCOPE.Name(dataset.scope), dataset.project, kwargs["token_info"])

    if body is None:
        body = {}

    query = body.get("query", {})
    query["dataset"] = id_
    response = stub.SearchVersions(dataset_pb2.SearchVersionRequest(
        query=query,
        page=body.get("page", 1),
        limit=body.get("limit", 25)
    ))

    return util.deserialize_protobuf(response)


@catch_exception
def list_datasets(body, **kwargs):
    """List datasets
    :param body:
    :type body: dict | bytes

    :rtype: PageLimitListSerializer
    """
    stub = get_datasets_services_stub()
    query = body.get("query")
    if query.get("scope") == "Local" and not query.get("project"):
        return ErrorSerializer(status=404,
                               title="Bad request",
                               detail="missing project for Local dataset."), 404

    check_dataset_permission(query.get("scope"), query.get("project"), kwargs["token_info"])
    response = stub.SearchDatasets(dataset_pb2.SearchDatasetRequest(**body))
    return util.deserialize_protobuf(response)


@catch_exception
def retrieve_dataset(id_, **kwargs):
    """Retrieve a dataset
    :param id_: The ID of the dataset resource
    :type id_: str

    :rtype: DatasetSerializer
    """
    stub = get_datasets_services_stub()
    dataset = stub.RetrieveDataset(dataset_pb2.ID(id=id_))
    check_dataset_permission(dataset_pb2.SCOPE.Name(dataset.scope), dataset.project, kwargs["token_info"])

    return DatasetSerializer.from_dict(util.deserialize_protobuf(dataset))


@catch_exception
def update_dataset(id_, body, **kwargs):
    """Update a dataset

    :param id_: The ID of the dataset resource
    :type id_: str
    :param body:
    :type body: dict | bytes

    :rtype: DatasetSerializer
    """
    stub = get_datasets_services_stub()
    dataset = stub.RetrieveDataset(dataset_pb2.ID(id=id_))
    check_dataset_permission(dataset_pb2.SCOPE.Name(dataset.scope),
                             dataset.project, kwargs["token_info"])

    dataset.name = body.get("name") if body.get("name") else dataset.name
    dataset.description = body.get("description") if body.get("description") else dataset.description

    dataset = stub.UpdateDataset(dataset)
    return DatasetSerializer.from_dict(util.deserialize_protobuf(dataset))


