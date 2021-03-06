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
from apis_server.serializers.experiment_spec_serializer import ExperimentSpecSerializer
from apis_server.serializers.workspace_metadata_serializer import WorkspaceMetadataSerializer
from apis_server import util


class ExperimentSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, metadata=None, spec=None, id=None, state=None, uptime=None, create_at=None, last_update=None):  # noqa: E501
        """ExperimentSerializer - a model defined in OpenAPI

        :param metadata: The metadata of this ExperimentSerializer.  # noqa: E501
        :type metadata: WorkspaceMetadataSerializer
        :param spec: The spec of this ExperimentSerializer.  # noqa: E501
        :type spec: ExperimentSpecSerializer
        :param id: The id of this ExperimentSerializer.  # noqa: E501
        :type id: str
        :param state: The state of this ExperimentSerializer.  # noqa: E501
        :type state: str
        :param uptime: The uptime of this ExperimentSerializer.  # noqa: E501
        :type uptime: int
        :param create_at: The create_at of this ExperimentSerializer.  # noqa: E501
        :type create_at: str
        :param last_update: The last_update of this ExperimentSerializer.  # noqa: E501
        :type last_update: str
        """
        self.openapi_types = {
            'metadata': WorkspaceMetadataSerializer,
            'spec': ExperimentSpecSerializer,
            'id': str,
            'state': str,
            'uptime': int,
            'create_at': str,
            'last_update': str
        }

        self.attribute_map = {
            'metadata': 'metadata',
            'spec': 'spec',
            'id': 'id',
            'state': 'state',
            'uptime': 'uptime',
            'create_at': 'create_at',
            'last_update': 'last_update'
        }

        self._metadata = metadata
        self._spec = spec
        self._id = id
        self._state = state
        self._uptime = uptime
        self._create_at = create_at
        self._last_update = last_update

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Experiment of this ExperimentSerializer.  # noqa: E501
        :rtype: ExperimentSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def metadata(self):
        """Gets the metadata of this ExperimentSerializer.


        :return: The metadata of this ExperimentSerializer.
        :rtype: WorkspaceMetadataSerializer
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ExperimentSerializer.


        :param metadata: The metadata of this ExperimentSerializer.
        :type metadata: WorkspaceMetadataSerializer
        """
        if metadata is None:
            raise ValueError("Invalid value for `metadata`, must not be `None`")  # noqa: E501

        self._metadata = metadata

    @property
    def spec(self):
        """Gets the spec of this ExperimentSerializer.


        :return: The spec of this ExperimentSerializer.
        :rtype: ExperimentSpecSerializer
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ExperimentSerializer.


        :param spec: The spec of this ExperimentSerializer.
        :type spec: ExperimentSpecSerializer
        """
        if spec is None:
            raise ValueError("Invalid value for `spec`, must not be `None`")  # noqa: E501

        self._spec = spec

    @property
    def id(self):
        """Gets the id of this ExperimentSerializer.


        :return: The id of this ExperimentSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExperimentSerializer.


        :param id: The id of this ExperimentSerializer.
        :type id: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this ExperimentSerializer.


        :return: The state of this ExperimentSerializer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ExperimentSerializer.


        :param state: The state of this ExperimentSerializer.
        :type state: str
        """
        allowed_values = ["CREATED", "STARTING", "RUNNING", "ABORTED", "SUCCEEDED", "FAILED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def uptime(self):
        """Gets the uptime of this ExperimentSerializer.


        :return: The uptime of this ExperimentSerializer.
        :rtype: int
        """
        return self._uptime

    @uptime.setter
    def uptime(self, uptime):
        """Sets the uptime of this ExperimentSerializer.


        :param uptime: The uptime of this ExperimentSerializer.
        :type uptime: int
        """

        self._uptime = uptime

    @property
    def create_at(self):
        """Gets the create_at of this ExperimentSerializer.


        :return: The create_at of this ExperimentSerializer.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this ExperimentSerializer.


        :param create_at: The create_at of this ExperimentSerializer.
        :type create_at: str
        """

        self._create_at = create_at

    @property
    def last_update(self):
        """Gets the last_update of this ExperimentSerializer.


        :return: The last_update of this ExperimentSerializer.
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this ExperimentSerializer.


        :param last_update: The last_update of this ExperimentSerializer.
        :type last_update: str
        """

        self._last_update = last_update
