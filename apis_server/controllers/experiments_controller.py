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
from mlflow.entities import ViewType

from apis_server.decorators import catch_exception
from apis_server.serializers import ArtifactsSerializer, StatusSerializer
from apis_server.serializers.experiment_serializer import ExperimentSerializer
from apis_server import util, permissions, ErrorSerializer
from apis_server.serializers.file_serializer import FileSerializer
from apis_server.services import get_experiments_services_stub, get_projects_services_stub, query_elasticsearch, \
    get_mlflow_client
from protos import job_pb2, project_pb2


def check_experiment_permission(obj, token_info):
    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=obj.metadata.project))
    if not permissions.IsProjectMember.has_object_permission(token_info, project):
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")


def get_experiment_object(experiment_id):
    stub = get_experiments_services_stub()
    return stub.Get(job_pb2.ID(id=experiment_id))


@catch_exception
def fetch_experiment_logs(id_, **kwargs):
    """Fetch logs of a given experiment.

    :param id_: The ID of the experiment resource
    :type id_: str

    :rtype: dict
    """
    exp = get_experiment_object(id_)
    check_experiment_permission(exp, kwargs["token_info"])
    query = "ilyde-experiment-{}".format(exp.id)
    return query_elasticsearch(query)


@catch_exception
def get_experiment_artifacts(id_, **kwargs):
    """Get artifacts of a succeeded experiment.

    :param id_: The ID of the experiment resource
    :type id_: str

    :rtype: ArtifactsSerializer
    """
    exp = get_experiment_object(id_)
    check_experiment_permission(exp, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    all_experiments = [e.experiment_id for e in mlflow_client.list_experiments()]
    runs = mlflow_client.search_runs(experiment_ids=all_experiments,
                                     filter_string="tags.`ilyde.job` = '{}'".format(exp.id),
                                     run_view_type=ViewType.ALL)
    if not runs:
        return ArtifactsSerializer(data=[])

    run = runs[0]
    dirs = []
    data = []
    path = None
    while True:
        artifacts = mlflow_client.list_artifacts(run_id=run.info.run_id, path=path)
        for artifact in artifacts:
            if artifact.is_dir:
                dirs.append(artifact.path)
            else:
                data.append(FileSerializer(name=artifact.path, is_dir=artifact.is_dir, size=artifact.file_size))
        if not dirs:
            break

        path = dirs.pop(0)

    return ArtifactsSerializer(data=data)


@catch_exception
def get_experiment_results(id_, **kwargs):
    """Get results of a succeeded experiment.

    :param id_: The ID of the experiment resource
    :type id_: str

    :rtype: dict
    """
    exp = get_experiment_object(id_)
    check_experiment_permission(exp, kwargs["token_info"])

    mlflow_client = get_mlflow_client()
    all_experiments = [e.experiment_id for e in mlflow_client.list_experiments()]
    runs = mlflow_client.search_runs(experiment_ids=all_experiments,
                                     filter_string="tags.`ilyde.job` = '{}'".format(exp.id),
                                     run_view_type=ViewType.ALL)
    if not runs:
        return {}

    return runs[0].to_dictionary()


@catch_exception
def retrieve_experiment(id_, **kwargs):
    """Retrieve an experiment

    :param id_: The ID of the experiment resource
    :type id_: str

    :rtype: ExperimentSerializer
    """
    exp = get_experiment_object(id_)
    check_experiment_permission(exp, kwargs["token_info"])

    return ExperimentSerializer.from_dict(util.deserialize_protobuf(exp))


@catch_exception
def state_experiment(id_, **kwargs):
    """Get state of a experiment.

    :param id_: The ID of the experiment resource
    :type id_: str

    :rtype: dict
    """
    exp = get_experiment_object(id_)
    check_experiment_permission(exp, kwargs["token_info"])

    stub = get_experiments_services_stub()
    state = stub.State(job_pb2.ID(id=id_))

    return util.deserialize_protobuf(state)


@catch_exception
def stop_experiment(id_, **kwargs):
    """Stop a running experiment.

    :param id_: The ID of the experiment resource
    :type id_: str

    :rtype: StatusSerializer
    """

    exp = get_experiment_object(id_)
    check_experiment_permission(exp, kwargs["token_info"])

    stub = get_experiments_services_stub()
    response = stub.Stop(job_pb2.ID(id=id_))

    if response.status != 200:
        return ErrorSerializer(status=response.status, title="Api Error",
                               detail=response.message), response.status

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def submit_experiment(body, **kwargs):
    """Submit an experiment

    :param body: experiment payload
    :type body: dict | bytes

    :rtype: StatusSerializer
    """

    serializer = ExperimentSerializer.from_dict(body)
    check_experiment_permission(serializer, kwargs["token_info"])
    stub = get_experiments_services_stub()
    response = stub.Submit(job_pb2.Experiment(**body))

    if response.status != 200:
        return ErrorSerializer(status=response.status, title="Api Error",
                               detail=response.message), response.status

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))
