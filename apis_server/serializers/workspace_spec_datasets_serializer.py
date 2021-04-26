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


class WorkspaceSpecDatasetsSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, version=None, mount_output=False):  # noqa: E501
        """WorkspaceSpecDatasetsSerializer - a model defined in OpenAPI

        :param id: The id of this WorkspaceSpecDatasetsSerializer.  # noqa: E501
        :type id: str
        :param version: The version of this WorkspaceSpecDatasetsSerializer.  # noqa: E501
        :type version: str
        :param mount_output: The mount_output of this WorkspaceSpecDatasetsSerializer.  # noqa: E501
        :type mount_output: bool
        """
        self.openapi_types = {
            'id': str,
            'version': str,
            'mount_output': bool
        }

        self.attribute_map = {
            'id': 'id',
            'version': 'version',
            'mount_output': 'mount_output'
        }

        self._id = id
        self._version = version
        self._mount_output = mount_output

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Workspace_spec_datasets of this WorkspaceSpecDatasetsSerializer.  # noqa: E501
        :rtype: WorkspaceSpecDatasetsSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this WorkspaceSpecDatasetsSerializer.


        :return: The id of this WorkspaceSpecDatasetsSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WorkspaceSpecDatasetsSerializer.


        :param id: The id of this WorkspaceSpecDatasetsSerializer.
        :type id: str
        """

        self._id = id

    @property
    def version(self):
        """Gets the version of this WorkspaceSpecDatasetsSerializer.


        :return: The version of this WorkspaceSpecDatasetsSerializer.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WorkspaceSpecDatasetsSerializer.


        :param version: The version of this WorkspaceSpecDatasetsSerializer.
        :type version: str
        """

        self._version = version

    @property
    def mount_output(self):
        """Gets the mount_output of this WorkspaceSpecDatasetsSerializer.


        :return: The mount_output of this WorkspaceSpecDatasetsSerializer.
        :rtype: bool
        """
        return self._mount_output

    @mount_output.setter
    def mount_output(self, mount_output):
        """Sets the mount_output of this WorkspaceSpecDatasetsSerializer.


        :param mount_output: The mount_output of this WorkspaceSpecDatasetsSerializer.
        :type mount_output: bool
        """

        self._mount_output = mount_output
