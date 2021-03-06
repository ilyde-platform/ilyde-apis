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

from apis_server.decorators import catch_exception, check_permissions
from apis_server.permissions import IsAdmin
from apis_server.serializers.hardware_tier_serializer import HardwareTierSerializer
from apis_server.serializers.page_limit_list_serializer import PageLimitListSerializer
from apis_server.serializers.status_serializer import StatusSerializer
from apis_server import util, ErrorSerializer
from apis_server.services import get_environments_services_stub
from protos import job_pb2


@catch_exception
@check_permissions(permissions=[IsAdmin])
def create_hardwaretier(body, **kwargs):
    """Create HardwareTier

    :param body: HardwareTier payload
    :type body: dict | bytes
    :rtype: HardwareTierSerializer
    """
    stub = get_environments_services_stub()
    hw = stub.CreateHardwareTier(job_pb2.HardwareTier(**body))

    return HardwareTierSerializer.from_dict(util.deserialize_protobuf(hw))


@catch_exception
@check_permissions(permissions=[IsAdmin])
def delete_hardwaretier(id_, **kwargs):
    """Delete HardwareTier
    :param id_: The ID of the hardware resource
    :type id_: str

    :rtype: StatusSerializer
    """
    stub = get_environments_services_stub()
    response = stub.DeleteHardwareTier(job_pb2.ID(id=id_))

    if response.status != 200:
        return ErrorSerializer(status=response.status, title="Api Error",
                               detail=response.message), response.status

    return StatusSerializer.from_dict(util.deserialize_protobuf(response))


@catch_exception
def list_environments(limit=None, page=None, **kwargs):
    """List available compute environments

    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageLimitListSerializer
    """
    stub = get_environments_services_stub()
    res = stub.ListEnvironments(job_pb2.Pagination(page=page, limit=limit))
    return util.deserialize_protobuf(res)


@catch_exception
def list_hardwaretiers(limit=None, page=None, **kwargs):
    """List available HardwareTiers

    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageLimitListSerializer
    """
    stub = get_environments_services_stub()
    res = stub.ListHardwareTiers(job_pb2.Pagination(page=page, limit=limit))
    return util.deserialize_protobuf(res)


@catch_exception
def list_ide(limit=None, page=None, **kwargs):
    """List available Ide for workspaces
    :param limit: 
    :type limit: int
    :param page: 
    :type page: int

    :rtype: PageLimitListSerializer
    """
    stub = get_environments_services_stub()
    res = stub.ListWorkspaceIde(job_pb2.Pagination(page=page, limit=limit))
    return util.deserialize_protobuf(res)


@catch_exception
def retrieve_hardwaretier(id_, **kwargs):  # noqa: E501
    """Retrieve HardwareTier
    :param id_: The ID of the hardware resource
    :type id_: str

    :rtype: HardwareTierSerializer
    """
    stub = get_environments_services_stub()
    res = stub.GetHardwareTier(job_pb2.ID(id=id_))
    return HardwareTierSerializer.from_dict(util.deserialize_protobuf(res))


@catch_exception
@check_permissions(permissions=[IsAdmin])
def update_hardwaretier(id_, body, **kwargs):  # noqa: E501
    """Update HardwareTier

    :param id_: The ID of the hardware resource
    :type id_: str
    :param body: HardwareTier payload
    :type body: dict | bytes

    :rtype: HardwareTierSerializer
    """
    hw = retrieve_hardwaretier(id_, **kwargs)
    hw.name = body["name"]
    hw.cores = body["cores"]
    hw.memory = body["memory"]
    hw.instancegroup = body["instancegroup"]
    hw.is_default = body["is_default"]
    hw.deployment = body["deployment"]

    stub = get_environments_services_stub()
    res = stub.UpdateHardwareTier(job_pb2.HardwareTier(**hw.to_dict()))
    return HardwareTierSerializer.from_dict(util.deserialize_protobuf(res))


