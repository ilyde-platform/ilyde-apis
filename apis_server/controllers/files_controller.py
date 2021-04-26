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
import mimetypes
import os

import connexion
import six
from flask import make_response, current_app
from mlflow.entities import ViewType

from apis_server.decorators import catch_exception
from apis_server.permissions import IsProjectMember
from apis_server.serializers.error_serializer import ErrorSerializer
from apis_server import util, services
from apis_server.services import get_projects_services_stub, get_mlflow_client, get_experiments_services_stub
from protos import project_pb2, job_pb2


@catch_exception
def get_experiment_artifact(id_, path, **kwargs):  # noqa: E501
    """Download experiment artifact

    Download experiment artifact

    :param id_: The ID of the experiment resource
    :type id_: str
    :param path: File's path to download
    :type path: str

    :rtype: file
    """
    stub = get_experiments_services_stub()
    experiment = stub.Get(job_pb2.ID(id=id_))

    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=experiment.metadata.project))
    if not IsProjectMember.has_object_permission(kwargs["token_info"], project):
        return ErrorSerializer(status=403,
                               title="Permission Denied",
                               detail="Doesn't have enough permissions to take this action"), 403

    mlflow_client = get_mlflow_client()

    all_experiments = [exp.experiment_id for exp in mlflow_client.list_experiments()]
    run = mlflow_client.search_runs(experiment_ids=all_experiments,
                                    filter_string="tags.`ilyde.job` = '{}'".format(experiment.id),
                                    run_view_type=ViewType.ALL)[0]

    local_dir = os.path.dirname(os.path.join(current_app.config.get("BASE_DIR"), "media", run.info.run_id, path))
    if not os.path.exists(local_dir):
        os.makedirs(local_dir, exist_ok=True)

    local_path = mlflow_client.download_artifacts(run.info.run_id, path, local_dir)
    file_type, _ = mimetypes.guess_type(local_path)
    if file_type is None:
        file_type = 'application/octet-stream'

    with open(local_path, 'rb') as f:
        response = make_response(f.read())
        response.headers.set('Content-Type', file_type)
        return response, 200


@catch_exception
def get_project_file(id_, path, version, **kwargs):
    """Download project's file

    Download project's file

    :param id_: The ID of the project resource
    :type id_: str
    :param path: File's path to download
    :type version: str
    :param version: File's version to download
    :type version: str

    :rtype: file
    """
    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=id_))
    if not IsProjectMember.has_object_permission(kwargs["token_info"], project):
        return ErrorSerializer(status=403,
                               title="Permission Denied",
                               detail="Doesn't have enough permissions to take this action"), 403

    extra_params = {}
    if version is not None:
        extra_params['version_id'] = version

    client = services.get_minio_client()

    data = client.get_object(project.repo_bucket, path, **extra_params)

    if int(data.getheader('Content-Length')) > 1024 * 1024 * 30:
        return ErrorSerializer(status=400, title="Bad Request",
                               detail="File is too large."), 400

    response = make_response(data.read())
    response.headers.set('Content-Type', data.getheader('Content-Type'))

    return response, 200

