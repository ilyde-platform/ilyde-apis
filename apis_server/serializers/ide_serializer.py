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


class IdeSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, image=None, title=None):  # noqa: E501
        """IdeSerializer - a model defined in OpenAPI

        :param id: The id of this IdeSerializer.  # noqa: E501
        :type id: str
        :param image: The image of this IdeSerializer.  # noqa: E501
        :type image: str
        :param title: The title of this IdeSerializer.  # noqa: E501
        :type title: str
        """
        self.openapi_types = {
            'id': str,
            'image': str,
            'title': str
        }

        self.attribute_map = {
            'id': 'id',
            'image': 'image',
            'title': 'title'
        }

        self._id = id
        self._image = image
        self._title = title

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Ide of this IdeSerializer.  # noqa: E501
        :rtype: IdeSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this IdeSerializer.


        :return: The id of this IdeSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this IdeSerializer.


        :param id: The id of this IdeSerializer.
        :type id: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this IdeSerializer.


        :return: The image of this IdeSerializer.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this IdeSerializer.


        :param image: The image of this IdeSerializer.
        :type image: str
        """

        self._image = image

    @property
    def title(self):
        """Gets the title of this IdeSerializer.


        :return: The title of this IdeSerializer.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IdeSerializer.


        :param title: The title of this IdeSerializer.
        :type title: str
        """

        self._title = title
