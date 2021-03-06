# coding: utf-8
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

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apis_server.serializers.base_model_ import Model
from apis_server.serializers.workspace_metadata_serializer import WorkspaceMetadataSerializer
from apis_server.serializers.workspace_spec_serializer import WorkspaceSpecSerializer
from apis_server import util


class WorkspaceSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, metadata=None, spec=None, id=None, state=None, uptime=None, create_at=None, last_start=None, last_update=None):  # noqa: E501
        """WorkspaceSerializer - a model defined in OpenAPI

        :param metadata: The metadata of this WorkspaceSerializer.  # noqa: E501
        :type metadata: WorkspaceMetadataSerializer
        :param spec: The spec of this WorkspaceSerializer.  # noqa: E501
        :type spec: WorkspaceSpecSerializer
        :param id: The id of this WorkspaceSerializer.  # noqa: E501
        :type id: str
        :param state: The state of this WorkspaceSerializer.  # noqa: E501
        :type state: str
        :param uptime: The uptime of this WorkspaceSerializer.  # noqa: E501
        :type uptime: int
        :param create_at: The create_at of this WorkspaceSerializer.  # noqa: E501
        :type create_at: str
        :param last_start: The last_start of this WorkspaceSerializer.  # noqa: E501
        :type last_start: str
        :param last_update: The last_update of this WorkspaceSerializer.  # noqa: E501
        :type last_update: str
        """
        self.openapi_types = {
            'metadata': WorkspaceMetadataSerializer,
            'spec': WorkspaceSpecSerializer,
            'id': str,
            'state': str,
            'uptime': int,
            'create_at': str,
            'last_start': str,
            'last_update': str
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'spec': 'spec',
            'id': 'id',
            'state': 'state',
            'uptime': 'uptime',
            'create_at': 'create_at',
            'last_start': 'last_start',
            'last_update': 'last_update'
        }

        self._metadata = metadata
        self._spec = spec
        self._id = id
        self._state = state
        self._uptime = uptime
        self._create_at = create_at
        self._last_start = last_start
        self._last_update = last_update

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Workspace of this WorkspaceSerializer.  # noqa: E501
        :rtype: WorkspaceSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self):
        """Gets the metadata of this WorkspaceSerializer.


        :return: The metadata of this WorkspaceSerializer.
        :rtype: WorkspaceMetadataSerializer
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this WorkspaceSerializer.


        :param metadata: The metadata of this WorkspaceSerializer.
        :type metadata: WorkspaceMetadataSerializer
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this WorkspaceSerializer.


        :return: The spec of this WorkspaceSerializer.
        :rtype: WorkspaceSpecSerializer
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this WorkspaceSerializer.


        :param spec: The spec of this WorkspaceSerializer.
        :type spec: WorkspaceSpecSerializer
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def id(self):
        """Gets the id of this WorkspaceSerializer.


        :return: The id of this WorkspaceSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceSerializer.


        :param id: The id of this WorkspaceSerializer.
        :type id: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this WorkspaceSerializer.


        :return: The state of this WorkspaceSerializer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WorkspaceSerializer.


        :param state: The state of this WorkspaceSerializer.
        :type state: str
        """
        allowed_values = ["CREATED", "STARTING", "RUNNING", "STOPPED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def uptime(self):
        """Gets the uptime of this WorkspaceSerializer.


        :return: The uptime of this WorkspaceSerializer.
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this WorkspaceSerializer.


        :param uptime: The uptime of this WorkspaceSerializer.
        :type uptime: int
        """

        self._uptime = uptime

    @property
    def create_at(self):
        """Gets the create_at of this WorkspaceSerializer.


        :return: The create_at of this WorkspaceSerializer.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this WorkspaceSerializer.


        :param create_at: The create_at of this WorkspaceSerializer.
        :type create_at: str
        """

        self._create_at = create_at

    @property
    def last_start(self):
        """Gets the last_start of this WorkspaceSerializer.


        :return: The last_start of this WorkspaceSerializer.
        :rtype: str
        """
        return self._last_start

    @last_start.setter
    def last_start(self, last_start):
        """Sets the last_start of this WorkspaceSerializer.


        :param last_start: The last_start of this WorkspaceSerializer.
        :type last_start: str
        """

        self._last_start = last_start

    @property
    def last_update(self):
        """Gets the last_update of this WorkspaceSerializer.


        :return: The last_update of this WorkspaceSerializer.
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this WorkspaceSerializer.


        :param last_update: The last_update of this WorkspaceSerializer.
        :type last_update: str
        """

        self._last_update = last_update
