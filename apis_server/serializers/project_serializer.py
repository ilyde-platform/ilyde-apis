# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apis_server.serializers.base_model_ import Model
from apis_server import util


class ProjectSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name=None, description=None, visibility=None, template=None, id=None, state=None, owner=None, members=None, repo_bucket=None, create_at=None, last_update=None):  # noqa: E501
        """ProjectSerializer - a model defined in OpenAPI

        :param name: The name of this ProjectSerializer.  # noqa: E501
        :type name: str
        :param description: The description of this ProjectSerializer.  # noqa: E501
        :type description: str
        :param visibility: The visibility of this ProjectSerializer.  # noqa: E501
        :type visibility: str
        :param template: The template of this ProjectSerializer.  # noqa: E501
        :type template: str
        :param id: The id of this ProjectSerializer.  # noqa: E501
        :type id: str
        :param state: The state of this ProjectSerializer.  # noqa: E501
        :type state: str
        :param owner: The owner of this ProjectSerializer.  # noqa: E501
        :type owner: str
        :param members: The members of this ProjectSerializer.  # noqa: E501
        :type members: List[str]
        :param repo_bucket: The repo_bucket of this ProjectSerializer.  # noqa: E501
        :type repo_bucket: str
        :param create_at: The create_at of this ProjectSerializer.  # noqa: E501
        :type create_at: str
        :param last_update: The last_update of this ProjectSerializer.  # noqa: E501
        :type last_update: str
        """
        self.openapi_types = {
            'name': str,
            'description': str,
            'visibility': str,
            'template': str,
            'id': str,
            'state': str,
            'owner': str,
            'members': List[str],
            'repo_bucket': str,
            'create_at': str,
            'last_update': str
        }

        self.attribute_map = {
            'name': 'name',
            'description': 'description',
            'visibility': 'visibility',
            'template': 'template',
            'id': 'id',
            'state': 'state',
            'owner': 'owner',
            'members': 'members',
            'repo_bucket': 'repo_bucket',
            'create_at': 'create_at',
            'last_update': 'last_update'
        }

        self._name = name
        self._description = description
        self._visibility = visibility
        self._template = template
        self._id = id
        self._state = state
        self._owner = owner
        self._members = members
        self._repo_bucket = repo_bucket
        self._create_at = create_at
        self._last_update = last_update

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Project of this ProjectSerializer.  # noqa: E501
        :rtype: ProjectSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this ProjectSerializer.


        :return: The name of this ProjectSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProjectSerializer.


        :param name: The name of this ProjectSerializer.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ProjectSerializer.


        :return: The description of this ProjectSerializer.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProjectSerializer.


        :param description: The description of this ProjectSerializer.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")  # noqa: E501

        self._description = description

    @property
    def visibility(self):
        """Gets the visibility of this ProjectSerializer.


        :return: The visibility of this ProjectSerializer.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        """Sets the visibility of this ProjectSerializer.


        :param visibility: The visibility of this ProjectSerializer.
        :type visibility: str
        """
        allowed_values = ["PRIVATE", "PUBLIC"]  # noqa: E501
        if visibility not in allowed_values:
            raise ValueError(
                "Invalid value for `visibility` ({0}), must be one of {1}"
                .format(visibility, allowed_values)
            )

        self._visibility = visibility

    @property
    def template(self):
        """Gets the template of this ProjectSerializer.


        :return: The template of this ProjectSerializer.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this ProjectSerializer.


        :param template: The template of this ProjectSerializer.
        :type template: str
        """
        allowed_values = ["GENERIC"]  # noqa: E501
        if template not in allowed_values:
            raise ValueError(
                "Invalid value for `template` ({0}), must be one of {1}"
                .format(template, allowed_values)
            )

        self._template = template

    @property
    def id(self):
        """Gets the id of this ProjectSerializer.


        :return: The id of this ProjectSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProjectSerializer.


        :param id: The id of this ProjectSerializer.
        :type id: str
        """

        self._id = id

    @property
    def state(self):
        """Gets the state of this ProjectSerializer.


        :return: The state of this ProjectSerializer.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ProjectSerializer.


        :param state: The state of this ProjectSerializer.
        :type state: str
        """
        allowed_values = ["OPEN", "CLOSED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def owner(self):
        """Gets the owner of this ProjectSerializer.


        :return: The owner of this ProjectSerializer.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this ProjectSerializer.


        :param owner: The owner of this ProjectSerializer.
        :type owner: str
        """

        self._owner = owner

    @property
    def members(self):
        """Gets the members of this ProjectSerializer.


        :return: The members of this ProjectSerializer.
        :rtype: List[str]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ProjectSerializer.


        :param members: The members of this ProjectSerializer.
        :type members: List[str]
        """

        self._members = members

    @property
    def repo_bucket(self):
        """Gets the repo_bucket of this ProjectSerializer.


        :return: The repo_bucket of this ProjectSerializer.
        :rtype: str
        """
        return self._repo_bucket

    @repo_bucket.setter
    def repo_bucket(self, repo_bucket):
        """Sets the repo_bucket of this ProjectSerializer.


        :param repo_bucket: The repo_bucket of this ProjectSerializer.
        :type repo_bucket: str
        """

        self._repo_bucket = repo_bucket

    @property
    def create_at(self):
        """Gets the create_at of this ProjectSerializer.


        :return: The create_at of this ProjectSerializer.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this ProjectSerializer.


        :param create_at: The create_at of this ProjectSerializer.
        :type create_at: str
        """

        self._create_at = create_at

    @property
    def last_update(self):
        """Gets the last_update of this ProjectSerializer.


        :return: The last_update of this ProjectSerializer.
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this ProjectSerializer.


        :param last_update: The last_update of this ProjectSerializer.
        :type last_update: str
        """

        self._last_update = last_update