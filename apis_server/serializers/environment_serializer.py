# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apis_server.serializers.base_model_ import Model
from apis_server import util


class EnvironmentSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, image=None, name=None, deployment=None):  # noqa: E501
        """EnvironmentSerializer - a model defined in OpenAPI

        :param id: The id of this EnvironmentSerializer.  # noqa: E501
        :type id: str
        :param image: The image of this EnvironmentSerializer.  # noqa: E501
        :type image: str
        :param name: The name of this EnvironmentSerializer.  # noqa: E501
        :type name: str
        :param deployment: The deployment of this EnvironmentSerializer.  # noqa: E501
        :type deployment: bool
        """
        self.openapi_types = {
            'id': str,
            'image': str,
            'name': str,
            'deployment': bool
        }

        self.attribute_map = {
            'id': 'id',
            'image': 'image',
            'name': 'name',
            'deployment': 'deployment'
        }

        self._id = id
        self._image = image
        self._name = name
        self._deployment = deployment

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Environment of this EnvironmentSerializer.  # noqa: E501
        :rtype: EnvironmentSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this EnvironmentSerializer.


        :return: The id of this EnvironmentSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EnvironmentSerializer.


        :param id: The id of this EnvironmentSerializer.
        :type id: str
        """

        self._id = id

    @property
    def image(self):
        """Gets the image of this EnvironmentSerializer.


        :return: The image of this EnvironmentSerializer.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this EnvironmentSerializer.


        :param image: The image of this EnvironmentSerializer.
        :type image: str
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this EnvironmentSerializer.


        :return: The name of this EnvironmentSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EnvironmentSerializer.


        :param name: The name of this EnvironmentSerializer.
        :type name: str
        """

        self._name = name

    @property
    def deployment(self):
        """Gets the deployment of this EnvironmentSerializer.


        :return: The deployment of this EnvironmentSerializer.
        :rtype: bool
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this EnvironmentSerializer.


        :param deployment: The deployment of this EnvironmentSerializer.
        :type deployment: bool
        """

        self._deployment = deployment
