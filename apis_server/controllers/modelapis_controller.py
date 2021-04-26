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
import json

import connexion
import six

from apis_server.decorators import catch_exception
from apis_server.serializers.error_serializer import ErrorSerializer
from apis_server.serializers.model_api_serializer import ModelApiSerializer
from apis_server.serializers.status_serializer import StatusSerializer
from apis_server import util, permissions
from apis_server.services import get_projects_services_stub, get_modelapis_services_stub, query_elasticsearch, \
    get_mlflow_client
from protos import project_pb2, job_pb2


def check_modelapi_permission(obj, token_info):
    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=obj.metadata.project))
    if not permissions.IsProjectMember.has_object_permission(token_info, project):
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")


def get_modelapi_object(modelapi_id):
    stub = get_modelapis_services_stub()
    return stub.Retrieve(job_pb2.ID(id=modelapi_id))


@catch_exception
def create_modelapi(body, **kwargs):
    """Create a modelapi

    :param body: modelapi payload
    :type body: dict | bytes

    :rtype: ModelApiSerializer
    """
    serializer = ModelApiSerializer.from_dict(body)
    check_modelapi_permission(serializer, kwargs["token_info"])

    stub = get_modelapis_services_stub()
    response = stub.Create(job_pb2.ModelApis(**body))

    return ModelApiSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def delete_modelapi(id_, **kwargs):
    """Delete a modelapi

    :param id_: The ID of the modelapi resource
    :type id_: str

    :rtype: StatusSerializer
    """
    modelapi = get_modelapi_object(id_)
    check_modelapi_permission(modelapi, kwargs["token_info"])
    stub = get_modelapis_services_stub()
    response = stub.Delete(job_pb2.ID(id=id_))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def fetch_modelapi_logs(id_, **kwargs):
    """Fetch logs of a given modelapi.

    :param id_: The ID of the modelapi resource
    :type id_: str

    :rtype: object
    """
    modelapi = get_modelapi_object(id_)
    query = "ilyde-modelapis-{}".format(modelapi.id)

    return query_elasticsearch(query)


@catch_exception
def list_modelapis(body=None, **kwargs):
    """List modelapis

    :param body:
    :type body: dict | bytes

    :rtype: PageLimitListSerializer
    """
    payload = body

    if body is None:
        payload = {"query": {}}

    stub = get_modelapis_services_stub()
    response = stub.Search(job_pb2.SearchRequest(**payload))

    return util.deserialize_protobuf(response)


@catch_exception
def retrieve_modelapi(id_, **kwargs):
    """Retrieve a modelapi

    :param id_: The ID of the modelapi resource
    :type id_: str

    :rtype: ModelApiSerializer
    """

    modelapi = get_modelapi_object(id_)
    return ModelApiSerializer.from_dict(util.deserialize_protobuf(modelapi))


@catch_exception
def signature_modelapi(id_, **kwargs):
    """Get signature of modelapi

    :param id_: The ID of the modelapi resource
    :type id_: str

    :rtype: object
    """
    modelapi = get_modelapi_object(id_)
    mlflow_client = get_mlflow_client()
    model_version = mlflow_client.get_model_version(modelapi.spec.model, modelapi.spec.version)
    run = mlflow_client.get_run(run_id=model_version.run_id)

    model_spec = json.loads(run.data.tags.get("mlflow.log-model.history"))[0]
    return model_spec.get("signature", {})


@catch_exception
def start_modelapi(id_, **kwargs):
    """Start a job
    :param id_: The ID of the modelapi resource
    :type id_: str

    :rtype: StatusSerializer
    """
    modelapi = get_modelapi_object(id_)
    check_modelapi_permission(modelapi, kwargs["token_info"])
    stub = get_modelapis_services_stub()
    response = stub.Start(job_pb2.ID(id=id_))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def status_modelapi(id_, **kwargs):
    """Get state of modelapi.
    :param id_: The ID of the modelapi resource
    :type id_: str

    :rtype: object
    """

    modelapi = get_modelapi_object(id_)
    check_modelapi_permission(modelapi, kwargs["token_info"])
    stub = get_modelapis_services_stub()
    response = stub.State(job_pb2.ID(id=id_))

    return util.deserialize_protobuf(response)


@catch_exception
def stop_modelapi(id_, **kwargs):
    """Stop a running modelapi.

    :param id_: The ID of the modelapi resource
    :type id_: str

    :rtype: StatusSerializer
    """
    modelapi = get_modelapi_object(id_)
    check_modelapi_permission(modelapi, kwargs["token_info"])
    stub = get_modelapis_services_stub()
    response = stub.Stop(job_pb2.ID(id=id_))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))
