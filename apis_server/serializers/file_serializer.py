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


class FileSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, size=0, is_dir=False):  # noqa: E501
        """FileSerializer - a model defined in OpenAPI

        :param files: The files of this FileSerializer.  # noqa: E501
        :type files: List
        """
        self.openapi_types = {
            'name': str,
            'size': int,
            'is_dir': bool,
        }

        self.attribute_map = {
            'name': 'name',
            'size': 'size',
            'is_dir': 'is_dir'
        }

        self._name = name
        self._size = size
        self._is_dir = is_dir

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The File of this FileSerializer.  # noqa: E501
        :rtype: FileSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this FileSerializer.


        :return: The name of this FileSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FileSerializer.


        :param name: The name of this FileSerializer.
        :type name: str
        """

        self._name = name

    @property
    def size(self):
        """Gets the size of this FileSerializer.


        :return: The size of this FileSerializer.
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this FileSerializer.


        :param size: The size of this FileSerializer.
        :type size: int
        """

        self._size = size

    @property
    def is_dir(self):
        """Gets the is_dir of this FileSerializer.


        :return: The is_dir of this FileSerializer.
        :rtype: bool
        """
        return self._is_dir

    @is_dir.setter
    def is_dir(self, is_dir):
        """Sets the is_dir of this FileSerializer.


        :param is_dir: The is_dir of this FileSerializer.
        :type is_dir: int
        """

        self._is_dir = is_dir
