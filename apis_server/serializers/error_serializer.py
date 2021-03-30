# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apis_server.serializers.base_model_ import Model
from apis_server import util


class ErrorSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, status=None, title=None, detail=None):  # noqa: E501
        """ErrorSerializer - a model defined in OpenAPI

        :param status: The status of this ErrorSerializer.  # noqa: E501
        :type status: int
        :param title: The title of this ErrorSerializer.  # noqa: E501
        :type title: str
        :param detail: The detail of this ErrorSerializer.  # noqa: E501
        :type detail: str
        """
        self.openapi_types = {
            'status': int,
            'title': str,
            'detail': str
        }

        self.attribute_map = {
            'status': 'status',
            'title': 'title',
            'detail': 'detail'
        }

        self._status = status
        self._title = title
        self._detail = detail

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Error of this ErrorSerializer.  # noqa: E501
        :rtype: ErrorSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def status(self):
        """Gets the status of this ErrorSerializer.


        :return: The status of this ErrorSerializer.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ErrorSerializer.


        :param status: The status of this ErrorSerializer.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def title(self):
        """Gets the title of this ErrorSerializer.


        :return: The title of this ErrorSerializer.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ErrorSerializer.


        :param title: The title of this ErrorSerializer.
        :type title: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def detail(self):
        """Gets the detail of this ErrorSerializer.


        :return: The detail of this ErrorSerializer.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this ErrorSerializer.


        :param detail: The detail of this ErrorSerializer.
        :type detail: str
        """
        if detail is None:
            raise ValueError("Invalid value for `detail`, must not be `None`")  # noqa: E501

        self._detail = detail