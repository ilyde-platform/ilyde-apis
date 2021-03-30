# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apis_server.serializers.base_model_ import Model
from apis_server.serializers.workspace_spec_datasets_serializer import WorkspaceSpecDatasetsSerializer
from apis_server import util


class RunSpecSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, revision=None, command=None, environment=None, hardware=None, datasets=None):  # noqa: E501
        """RunSpecSerializer - a model defined in OpenAPI

        :param revision: The revision of this RunSpecSerializer.  # noqa: E501
        :type revision: str
        :param command: The command of this RunSpecSerializer.  # noqa: E501
        :type command: str
        :param environment: The environment of this RunSpecSerializer.  # noqa: E501
        :type environment: str
        :param hardware: The hardware of this RunSpecSerializer.  # noqa: E501
        :type hardware: str
        :param datasets: The datasets of this RunSpecSerializer.  # noqa: E501
        :type datasets: List[WorkspaceSpecDatasetsSerializer]
        """
        self.openapi_types = {
            'revision': str,
            'command': str,
            'environment': str,
            'hardware': str,
            'datasets': List[WorkspaceSpecDatasetsSerializer]
        }

        self.attribute_map = {
            'revision': 'revision',
            'command': 'command',
            'environment': 'environment',
            'hardware': 'hardware',
            'datasets': 'datasets'
        }

        self._revision = revision
        self._command = command
        self._environment = environment
        self._hardware = hardware
        self._datasets = datasets

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Run_spec of this RunSpecSerializer.  # noqa: E501
        :rtype: RunSpecSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def revision(self):
        """Gets the revision of this RunSpecSerializer.


        :return: The revision of this RunSpecSerializer.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this RunSpecSerializer.


        :param revision: The revision of this RunSpecSerializer.
        :type revision: str
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def command(self):
        """Gets the command of this RunSpecSerializer.


        :return: The command of this RunSpecSerializer.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this RunSpecSerializer.


        :param command: The command of this RunSpecSerializer.
        :type command: str
        """
        if command is None:
            raise ValueError("Invalid value for `command`, must not be `None`")  # noqa: E501

        self._command = command

    @property
    def environment(self):
        """Gets the environment of this RunSpecSerializer.


        :return: The environment of this RunSpecSerializer.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this RunSpecSerializer.


        :param environment: The environment of this RunSpecSerializer.
        :type environment: str
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def hardware(self):
        """Gets the hardware of this RunSpecSerializer.


        :return: The hardware of this RunSpecSerializer.
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this RunSpecSerializer.


        :param hardware: The hardware of this RunSpecSerializer.
        :type hardware: str
        """
        if hardware is None:
            raise ValueError("Invalid value for `hardware`, must not be `None`")  # noqa: E501

        self._hardware = hardware

    @property
    def datasets(self):
        """Gets the datasets of this RunSpecSerializer.


        :return: The datasets of this RunSpecSerializer.
        :rtype: List[WorkspaceSpecDatasetsSerializer]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this RunSpecSerializer.


        :param datasets: The datasets of this RunSpecSerializer.
        :type datasets: List[WorkspaceSpecDatasetsSerializer]
        """

        self._datasets = datasets
