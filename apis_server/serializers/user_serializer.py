# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apis_server.serializers.base_model_ import Model
from apis_server import util


class UserSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, username=None, first_name=None, last_name=None, email=None, password=None, id=None, groups=None, email_verified=None, enabled=None, created_timestamp=None):  # noqa: E501
        """UserSerializer - a model defined in OpenAPI

        :param username: The username of this UserSerializer.  # noqa: E501
        :type username: str
        :param first_name: The first_name of this UserSerializer.  # noqa: E501
        :type first_name: str
        :param last_name: The last_name of this UserSerializer.  # noqa: E501
        :type last_name: str
        :param email: The email of this UserSerializer.  # noqa: E501
        :type email: str
        :param password: The password of this UserSerializer.  # noqa: E501
        :type password: str
        :param id: The id of this UserSerializer.  # noqa: E501
        :type id: str
        :param groups: The groups of this UserSerializer.  # noqa: E501
        :type groups: List[str]
        :param email_verified: The email_verified of this UserSerializer.  # noqa: E501
        :type email_verified: bool
        :param enabled: The enabled of this UserSerializer.  # noqa: E501
        :type enabled: bool
        :param created_timestamp: The created_timestamp of this UserSerializer.  # noqa: E501
        :type created_timestamp: str
        """
        self.openapi_types = {
            'username': str,
            'first_name': str,
            'last_name': str,
            'email': str,
            'password': str,
            'id': str,
            'groups': List[str],
            'email_verified': bool,
            'enabled': bool,
            'created_timestamp': str
        }

        self.attribute_map = {
            'username': 'username',
            'first_name': 'first_name',
            'last_name': 'last_name',
            'email': 'email',
            'password': 'password',
            'id': 'id',
            'groups': 'groups',
            'email_verified': 'email_verified',
            'enabled': 'enabled',
            'created_timestamp': 'createdTimestamp'
        }

        self._username = username
        self._first_name = first_name
        self._last_name = last_name
        self._email = email
        self._password = password
        self._id = id
        self._groups = groups
        self._email_verified = email_verified
        self._enabled = enabled
        self._created_timestamp = created_timestamp

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this UserSerializer.  # noqa: E501
        :rtype: UserSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def username(self):
        """Gets the username of this UserSerializer.


        :return: The username of this UserSerializer.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserSerializer.


        :param username: The username of this UserSerializer.
        :type username: str
        """
        if username is None:
            raise ValueError("Invalid value for `username`, must not be `None`")  # noqa: E501

        self._username = username

    @property
    def first_name(self):
        """Gets the first_name of this UserSerializer.


        :return: The first_name of this UserSerializer.
        :rtype: str
        """
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        """Sets the first_name of this UserSerializer.


        :param first_name: The first_name of this UserSerializer.
        :type first_name: str
        """
        if first_name is None:
            raise ValueError("Invalid value for `first_name`, must not be `None`")  # noqa: E501

        self._first_name = first_name

    @property
    def last_name(self):
        """Gets the last_name of this UserSerializer.


        :return: The last_name of this UserSerializer.
        :rtype: str
        """
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        """Sets the last_name of this UserSerializer.


        :param last_name: The last_name of this UserSerializer.
        :type last_name: str
        """
        if last_name is None:
            raise ValueError("Invalid value for `last_name`, must not be `None`")  # noqa: E501

        self._last_name = last_name

    @property
    def email(self):
        """Gets the email of this UserSerializer.


        :return: The email of this UserSerializer.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserSerializer.


        :param email: The email of this UserSerializer.
        :type email: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def password(self):
        """Gets the password of this UserSerializer.


        :return: The password of this UserSerializer.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this UserSerializer.


        :param password: The password of this UserSerializer.
        :type password: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501

        self._password = password

    @property
    def id(self):
        """Gets the id of this UserSerializer.


        :return: The id of this UserSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSerializer.


        :param id: The id of this UserSerializer.
        :type id: str
        """

        self._id = id

    @property
    def groups(self):
        """Gets the groups of this UserSerializer.


        :return: The groups of this UserSerializer.
        :rtype: List[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this UserSerializer.


        :param groups: The groups of this UserSerializer.
        :type groups: List[str]
        """

        self._groups = groups

    @property
    def email_verified(self):
        """Gets the email_verified of this UserSerializer.


        :return: The email_verified of this UserSerializer.
        :rtype: bool
        """
        return self._email_verified

    @email_verified.setter
    def email_verified(self, email_verified):
        """Sets the email_verified of this UserSerializer.


        :param email_verified: The email_verified of this UserSerializer.
        :type email_verified: bool
        """

        self._email_verified = email_verified

    @property
    def enabled(self):
        """Gets the enabled of this UserSerializer.


        :return: The enabled of this UserSerializer.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this UserSerializer.


        :param enabled: The enabled of this UserSerializer.
        :type enabled: bool
        """

        self._enabled = enabled

    @property
    def created_timestamp(self):
        """Gets the created_timestamp of this UserSerializer.


        :return: The created_timestamp of this UserSerializer.
        :rtype: str
        """
        return self._created_timestamp

    @created_timestamp.setter
    def created_timestamp(self, created_timestamp):
        """Sets the created_timestamp of this UserSerializer.


        :param created_timestamp: The created_timestamp of this UserSerializer.
        :type created_timestamp: str
        """

        self._created_timestamp = created_timestamp
