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


class DatasetSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, scope=None, id=None, project=None, version=None, create_at=None, last_update=None):  # noqa: E501
        """DatasetSerializer - a model defined in OpenAPI

        :param name: The name of this DatasetSerializer.  # noqa: E501
        :type name: str
        :param description: The description of this DatasetSerializer.  # noqa: E501
        :type description: str
        :param scope: The scope of this DatasetSerializer.  # noqa: E501
        :type scope: str
        :param id: The id of this DatasetSerializer.  # noqa: E501
        :type id: str
        :param project: The project of this DatasetSerializer.  # noqa: E501
        :type project: str
        :param version: The version of this DatasetSerializer.  # noqa: E501
        :type version: str
        :param create_at: The create_at of this DatasetSerializer.  # noqa: E501
        :type create_at: str
        :param last_update: The last_update of this DatasetSerializer.  # noqa: E501
        :type last_update: str
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'scope': str,
            'id': str,
            'project': str,
            'version': str,
            'create_at': str,
            'last_update': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'scope': 'scope',
            'id': 'id',
            'project': 'project',
            'version': 'version',
            'create_at': 'create_at',
            'last_update': 'last_update'
        }

        self._name = name
        self._description = description
        self._scope = scope
        self._id = id
        self._project = project
        self._version = version
        self._create_at = create_at
        self._last_update = last_update

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Dataset of this DatasetSerializer.  # noqa: E501
        :rtype: DatasetSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this DatasetSerializer.


        :return: The name of this DatasetSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetSerializer.


        :param name: The name of this DatasetSerializer.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this DatasetSerializer.


        :return: The description of this DatasetSerializer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DatasetSerializer.


        :param description: The description of this DatasetSerializer.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def scope(self):
        """Gets the scope of this DatasetSerializer.


        :return: The scope of this DatasetSerializer.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this DatasetSerializer.


        :param scope: The scope of this DatasetSerializer.
        :type scope: str
        """
        allowed_values = ["Local", "Global"]  # noqa: E501
        if scope not in allowed_values:
            raise ValueError(
                "Invalid value for `scope` ({0}), must be one of {1}"
                .format(scope, allowed_values)
            )

        self._scope = scope

    @property
    def id(self):
        """Gets the id of this DatasetSerializer.


        :return: The id of this DatasetSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetSerializer.


        :param id: The id of this DatasetSerializer.
        :type id: str
        """

        self._id = id

    @property
    def project(self):
        """Gets the project of this DatasetSerializer.


        :return: The project of this DatasetSerializer.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this DatasetSerializer.


        :param project: The project of this DatasetSerializer.
        :type project: str
        """

        self._project = project

    @property
    def version(self):
        """Gets the version of this DatasetSerializer.


        :return: The version of this DatasetSerializer.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DatasetSerializer.


        :param version: The version of this DatasetSerializer.
        :type version: str
        """

        self._version = version

    @property
    def create_at(self):
        """Gets the create_at of this DatasetSerializer.


        :return: The create_at of this DatasetSerializer.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this DatasetSerializer.


        :param create_at: The create_at of this DatasetSerializer.
        :type create_at: str
        """

        self._create_at = create_at

    @property
    def last_update(self):
        """Gets the last_update of this DatasetSerializer.


        :return: The last_update of this DatasetSerializer.
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this DatasetSerializer.


        :param last_update: The last_update of this DatasetSerializer.
        :type last_update: str
        """

        self._last_update = last_update
