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


class WorkspaceMetadataSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, project=None, owner=None, link=None):  # noqa: E501
        """WorkspaceMetadataSerializer - a model defined in OpenAPI

        :param name: The name of this WorkspaceMetadataSerializer.  # noqa: E501
        :type name: str
        :param project: The project of this WorkspaceMetadataSerializer.  # noqa: E501
        :type project: str
        :param owner: The owner of this WorkspaceMetadataSerializer.  # noqa: E501
        :type owner: str
        :param link: The link of this WorkspaceMetadataSerializer.  # noqa: E501
        :type link: str
        """
        self.openapi_types = {
            'name': str,
            'project': str,
            'owner': str,
            'link': str
        }

        self.attribute_map = {
            'name': 'name',
            'project': 'project',
            'owner': 'owner',
            'link': 'link'
        }

        self._name = name
        self._project = project
        self._owner = owner
        self._link = link

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Workspace_metadata of this WorkspaceMetadataSerializer.  # noqa: E501
        :rtype: WorkspaceMetadataSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this WorkspaceMetadataSerializer.


        :return: The name of this WorkspaceMetadataSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WorkspaceMetadataSerializer.


        :param name: The name of this WorkspaceMetadataSerializer.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def project(self):
        """Gets the project of this WorkspaceMetadataSerializer.


        :return: The project of this WorkspaceMetadataSerializer.
        :rtype: str
        """
        return self._project

    @project.setter
    def project(self, project):
        """Sets the project of this WorkspaceMetadataSerializer.


        :param project: The project of this WorkspaceMetadataSerializer.
        :type project: str
        """
        if project is None:
            raise ValueError("Invalid value for `project`, must not be `None`")  # noqa: E501

        self._project = project

    @property
    def owner(self):
        """Gets the owner of this WorkspaceMetadataSerializer.


        :return: The owner of this WorkspaceMetadataSerializer.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this WorkspaceMetadataSerializer.


        :param owner: The owner of this WorkspaceMetadataSerializer.
        :type owner: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")  # noqa: E501

        self._owner = owner

    @property
    def link(self):
        """Gets the link of this WorkspaceMetadataSerializer.


        :return: The link of this WorkspaceMetadataSerializer.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this WorkspaceMetadataSerializer.


        :param link: The link of this WorkspaceMetadataSerializer.
        :type link: str
        """

        self._link = link
