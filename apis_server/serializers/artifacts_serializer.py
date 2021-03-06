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
from apis_server.serializers.file_serializer import FileSerializer
from apis_server import util


class ArtifactsSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data=None):  # noqa: E501
        """ArtifactsSerializer - a model defined in OpenAPI

        :param data: The data of this ArtifactsSerializer.  # noqa: E501
        :type data: List[FileSerializer]
        """
        self.openapi_types = {
            'data': List[FileSerializer]
        }

        self.attribute_map = {
            'data': 'data'
        }

        self._data = data

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Artifacts of this ArtifactsSerializer.  # noqa: E501
        :rtype: ArtifactsSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ArtifactsSerializer.


        :return: The data of this ArtifactsSerializer.
        :rtype: List[FileSerializer]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ArtifactsSerializer.


        :param data: The data of this ArtifactsSerializer.
        :type data: List[FileSerializer]
        """

        self._data = data
