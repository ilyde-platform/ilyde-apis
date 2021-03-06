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


class FileVersionSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, version=None):  # noqa: E501
        """FileVersionSerializer - a model defined in OpenAPI

        :param name: The name of this FileVersionSerializer.  # noqa: E501
        :type name: str
        :param version: The version of this FileVersionSerializer.  # noqa: E501
        :type version: str
        """
        self.openapi_types = {
            'name': str,
            'version': str
        }

        self.attribute_map = {
            'name': 'name',
            'version': 'version'
        }

        self._name = name
        self._version = version

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileVersion of this FileVersionSerializer.  # noqa: E501
        :rtype: FileVersionSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this FileVersionSerializer.


        :return: The name of this FileVersionSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileVersionSerializer.


        :param name: The name of this FileVersionSerializer.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this FileVersionSerializer.


        :return: The version of this FileVersionSerializer.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this FileVersionSerializer.


        :param version: The version of this FileVersionSerializer.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version
