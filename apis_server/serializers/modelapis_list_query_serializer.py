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
from apis_server import util


class ModelapisListQuerySerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, state=None, owner=None, project=None):  # noqa: E501
        """ModelapisListQuerySerializer - a model defined in OpenAPI

        :param state: The state of this ModelapisListQuerySerializer.  # noqa: E501
        :type state: str
        :param owner: The owner of this ModelapisListQuerySerializer.  # noqa: E501
        :type owner: str
        :param project: The project of this ModelapisListQuerySerializer.  # noqa: E501
        :type project: str
        """
        self.openapi_types = {
            'state': str,
            'owner': str,
            'project': str
        }

        self.attribute_map = {
            'state': 'state',
            'owner': 'owner',
            'project': 'project'
        }

        self._state = state
        self._owner = owner
        self._project = project

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The _modelapis_list_query of this ModelapisListQuerySerializer.  # noqa: E501
        :rtype: ModelapisListQuerySerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def state(self):
        """Gets the state of this ModelapisListQuerySerializer.


        :return: The state of this ModelapisListQuerySerializer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ModelapisListQuerySerializer.


        :param state: The state of this ModelapisListQuerySerializer.
        :type state: str
        """

        self._state = state

    @property
    def owner(self):
        """Gets the owner of this ModelapisListQuerySerializer.


        :return: The owner of this ModelapisListQuerySerializer.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ModelapisListQuerySerializer.


        :param owner: The owner of this ModelapisListQuerySerializer.
        :type owner: str
        """

        self._owner = owner

    @property
    def project(self):
        """Gets the project of this ModelapisListQuerySerializer.


        :return: The project of this ModelapisListQuerySerializer.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this ModelapisListQuerySerializer.


        :param project: The project of this ModelapisListQuerySerializer.
        :type project: str
        """

        self._project = project
