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
from apis_server.serializers import StatusSerializer, PageTokenListSerializer
from apis_server.serializers.model_serializer import ModelSerializer
from apis_server.serializers.model_version_serializer import ModelVersionSerializer

from apis_server import util, permissions
from apis_server.services import get_projects_services_stub, get_mlflow_client
from protos import project_pb2


def check_model_permission(obj, token_info):
    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=obj.tags["ilyde.project"]))
    if not permissions.IsProjectMember.has_object_permission(token_info, project):
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")


def get_mlflow_model(name):
    mlflow_client = get_mlflow_client()
    return mlflow_client.get_registered_model(name)


@catch_exception
def create_model(body, **kwargs):
    """Create a model

    :param body: Request payload to create a model
    :type body: dict | bytes

    :rtype: ModelSerializer
    """
    serializer = ModelSerializer.from_dict(body)
    description = serializer.description if serializer.description else ""
    project_id = serializer.tags.get("ilyde.project")
    if not project_id:
        raise connexion.ProblemException(status=400, title="Bad Request",
                                         detail="ilyde.project tag should be provided with the id of the project.")

    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=project_id))
    if not permissions.IsProjectMember.has_object_permission(kwargs["token_info"], project):
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")

    model_name = util.safe_model_name(serializer.name)
    if not model_name.startswith(util.safe_model_name(project.name)):
        model_name = "{}-{}".format(util.safe_model_name(project.name), model_name)

    mlflow_client = get_mlflow_client()
    model = mlflow_client.create_registered_model(name=model_name, description=description, tags=serializer.tags)

    return ModelSerializer(
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
    )


@catch_exception
def create_model_version(name, body, **kwargs):
    """Create a model version

    :param name: The unique name of the model
    :type name: str
    :param body: Request payload to create a model version
    :type body: dict | bytes

    :rtype: ModelVersionSerializer
    """
    serializer = ModelVersionSerializer.from_dict(body)
    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()

    version = mlflow_client.create_model_version(
        name=name,
        source=serializer.source,
        run_id=serializer.run_id,
        tags=serializer.tags,
        description=serializer.description
    )

    return ModelVersionSerializer(
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
    )


@catch_exception
def delete_model(name, **kwargs):
    """Delete a model

    :param name: The unique name of the model
    :type name: str

    :rtype: StatusSerializer
    """
    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    mlflow_client.delete_registered_model(name)

    return StatusSerializer(status=200, message="successfully deleted")


@catch_exception
def delete_model_version(name, version, **kwargs):
    """delete a model version

    :param name: The unique name of the model
    :type name: str
    :param version: The version of the model to delete
    :type version: str

    :rtype: StatusSerializer
    """
    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    mlflow_client.delete_model_version(name, version)

    return StatusSerializer(status=200, message="successfully deleted")


@catch_exception
def get_model_version(name, version, **kwargs):
    """get a model version

    :param name: The unique name of the model
    :type name: str
    :param version: The version of the model to retrieve
    :type version: str

    :rtype: ModelVersionSerializer
    """

    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    version = mlflow_client.get_model_version(name, version)

    return ModelVersionSerializer(
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
    )


@catch_exception
def list_model_versions(name, **kwargs):
    """list versions of a model

    :param name: The unique name of the model
    :type name: str

    :rtype: PageTokenListSerializer
    """

    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    filter_string = "name='{}'".format(name)
    versions = mlflow_client.search_model_versions(filter_string)

    data = [ModelVersionSerializer(
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
    ) for version in versions]

    return PageTokenListSerializer(data=data, next_page_token="")


@catch_exception
def retrieve_model(name, **kwargs):
    """Retrieve a model

    :param name: The unique name of the model
    :type name: str

    :rtype: ModelSerializer
    """

    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    return ModelSerializer(
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
    )


@catch_exception
def transition_model_version_stage(name, version, body, **kwargs):
    """Transition model version stage

    :param name: The unique name of the model
    :type name: str
    :param version: The version of the model
    :type version: str
    :param body:
    :type body: dict | bytes

    :rtype: ModelVersionSerializer
    """
    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    version = mlflow_client.transition_model_version_stage(name, version, body["stage"])

    return ModelVersionSerializer(
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
        )


@catch_exception
def update_model(name, body, **kwargs):
    """Update a model

    :param name: The unique name of the model
    :type name: str
    :param body:
    :type body: dict | bytes

    :rtype: ModelSerializer
    """
    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    serializer = ModelSerializer.from_dict(body)
    model = mlflow_client.update_registered_model(name, description=serializer.description)

    return ModelSerializer(
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
    )


@catch_exception
def update_model_version(name, version, body=None, **kwargs):
    """update a model version

    :param name: The unique name of the model
    :type name: str
    :param version: The version of the model to retrieve
    :type version: str
    :param body:
    :type body: dict | bytes

    :rtype: ModelVersionSerializer
    """
    model = get_mlflow_model(name)
    check_model_permission(model, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    serializer = ModelVersionSerializer.from_dict(body)
    model_version = mlflow_client.update_model_version(name, version, description=serializer.description)
    ModelVersionSerializer(
        creation_timestamp=model_version.creation_timestamp,
        current_stage=model_version.current_stage,
        description=model_version.description,
        last_updated_timestamp=model_version.last_updated_timestamp,
        name=model_version.name,
        run_id=model_version.run_id,
        source=model_version.source,
        status=model_version.status,
        status_message=model_version.status_message,
        tags=model_version.tags,
        version=model_version.version
    )
