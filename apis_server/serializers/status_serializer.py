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


class StatusSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status=None, message=None):  # noqa: E501
        """StatusSerializer - a model defined in OpenAPI

        :param status: The status of this StatusSerializer.  # noqa: E501
        :type status: int
        :param message: The message of this StatusSerializer.  # noqa: E501
        :type message: str
        """
        self.openapi_types = {
            'status': int,
            'message': str
        }

        self.attribute_map = {
            'status': 'status',
            'message': 'message'
        }

        self._status = status
        self._message = message

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Status of this StatusSerializer.  # noqa: E501
        :rtype: StatusSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this StatusSerializer.


        :return: The status of this StatusSerializer.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this StatusSerializer.


        :param status: The status of this StatusSerializer.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def message(self):
        """Gets the message of this StatusSerializer.


        :return: The message of this StatusSerializer.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this StatusSerializer.


        :param message: The message of this StatusSerializer.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message
