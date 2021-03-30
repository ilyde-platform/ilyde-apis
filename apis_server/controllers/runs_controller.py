import connexion
import six

from apis_server.decorators import catch_exception
from apis_server.serializers import StatusSerializer
from apis_server.serializers.run_serializer import RunSerializer
from apis_server import util, permissions
from apis_server.services import get_projects_services_stub, get_runs_services_stub, query_elasticsearch
from protos import project_pb2, job_pb2


def check_run_permission(obj, token_info):
    stub = get_projects_services_stub()
    project = stub.Retrieve(project_pb2.ID(id=obj.metadata.project))
    if not permissions.IsProjectMember.has_object_permission(token_info, project):
        raise connexion.ProblemException(status=403, title="Permission Denied",
                                         detail="Doesn't have enough permissions to take this action")


def get_run_object(run_id):
    stub = get_runs_services_stub()
    return stub.Get(job_pb2.ID(id=run_id))


@catch_exception
def fetch_run_logs(id_, **kwargs):
    """Fetch logs of a given run.
    :param id_: The ID of the run resource
    :type id_: str

    :rtype: object
    """
    run = get_run_object(id_)
    check_run_permission(run, kwargs["token_info"])
    query = "ilyde-run-{}".format(run.id)
    return query_elasticsearch(query)


@catch_exception
def retrieve_run(id_, **kwargs):
    """Retrieve a run
    :param id_: The ID of the run resource
    :type id_: str

    :rtype: RunSerializer
    """
    run = get_run_object(id_)
    check_run_permission(run, kwargs["token_info"])
    return RunSerializer.from_dict(util.deserialize_protobuf(run))


def state_run(id_, **kwargs):
    """Get state of a run.
    :param id_: The ID of the run resource
    :type id_: str

    :rtype: Object
    """
    run = get_run_object(id_)
    check_run_permission(run, kwargs["token_info"])

    stub = get_runs_services_stub()
    state = stub.State(job_pb2.ID(id=id_))

    return util.deserialize_protobuf(state)


def stop_run(id_, **kwargs):
    """Stop a running run.
    :param id_: The ID of the run resource
    :type id_: str

    :rtype: StatusSerializer
    """
    run = get_run_object(id_)
    check_run_permission(run, kwargs["token_info"])

    stub = get_runs_services_stub()
    response = stub.Stop(job_pb2.ID(id=id_))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


def submit_run(body, **kwargs):
    """Submit a run
    :param body: run payload
    :type body: dict | bytes

    :rtype: StatusSerializer
    """
    serializer = RunSerializer.from_dict(body)
    check_run_permission(serializer, kwargs["token_info"])

    stub = get_runs_services_stub()
    response = stub.Submit(job_pb2.Run(**body))

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))
