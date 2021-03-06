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
from apis_server.serializers.experiment_spec_params_serializer import ExperimentSpecParamsSerializer
from apis_server.serializers.workspace_spec_datasets_serializer import WorkspaceSpecDatasetsSerializer
from apis_server import util


class ExperimentSpecSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, revision=None, entrypoint=None, environment=None, hardware=None, params=None, datasets=None):  # noqa: E501
        """ExperimentSpecSerializer - a model defined in OpenAPI

        :param revision: The revision of this ExperimentSpecSerializer.  # noqa: E501
        :type revision: str
        :param entrypoint: The entrypoint of this ExperimentSpecSerializer.  # noqa: E501
        :type entrypoint: str
        :param environment: The environment of this ExperimentSpecSerializer.  # noqa: E501
        :type environment: str
        :param hardware: The hardware of this ExperimentSpecSerializer.  # noqa: E501
        :type hardware: str
        :param params: The params of this ExperimentSpecSerializer.  # noqa: E501
        :type params: List[ExperimentSpecParamsSerializer]
        :param datasets: The datasets of this ExperimentSpecSerializer.  # noqa: E501
        :type datasets: List[WorkspaceSpecDatasetsSerializer]
        """
        self.openapi_types = {
            'revision': str,
            'entrypoint': str,
            'environment': str,
            'hardware': str,
            'params': List[ExperimentSpecParamsSerializer],
            'datasets': List[WorkspaceSpecDatasetsSerializer]
        }

        self.attribute_map = {
            'revision': 'revision',
            'entrypoint': 'entrypoint',
            'environment': 'environment',
            'hardware': 'hardware',
            'params': 'params',
            'datasets': 'datasets'
        }

        self._revision = revision
        self._entrypoint = entrypoint
        self._environment = environment
        self._hardware = hardware
        self._params = params
        self._datasets = datasets

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Experiment_spec of this ExperimentSpecSerializer.  # noqa: E501
        :rtype: ExperimentSpecSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def revision(self):
        """Gets the revision of this ExperimentSpecSerializer.


        :return: The revision of this ExperimentSpecSerializer.
        :rtype: str
        """
        return self._revision

    @revision.setter
    def revision(self, revision):
        """Sets the revision of this ExperimentSpecSerializer.


        :param revision: The revision of this ExperimentSpecSerializer.
        :type revision: str
        """
        if revision is None:
            raise ValueError("Invalid value for `revision`, must not be `None`")  # noqa: E501

        self._revision = revision

    @property
    def entrypoint(self):
        """Gets the entrypoint of this ExperimentSpecSerializer.


        :return: The entrypoint of this ExperimentSpecSerializer.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        """Sets the entrypoint of this ExperimentSpecSerializer.


        :param entrypoint: The entrypoint of this ExperimentSpecSerializer.
        :type entrypoint: str
        """
        if entrypoint is None:
            raise ValueError("Invalid value for `entrypoint`, must not be `None`")  # noqa: E501

        self._entrypoint = entrypoint

    @property
    def environment(self):
        """Gets the environment of this ExperimentSpecSerializer.


        :return: The environment of this ExperimentSpecSerializer.
        :rtype: str
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this ExperimentSpecSerializer.


        :param environment: The environment of this ExperimentSpecSerializer.
        :type environment: str
        """
        if environment is None:
            raise ValueError("Invalid value for `environment`, must not be `None`")  # noqa: E501

        self._environment = environment

    @property
    def hardware(self):
        """Gets the hardware of this ExperimentSpecSerializer.


        :return: The hardware of this ExperimentSpecSerializer.
        :rtype: str
        """
        return self._hardware

    @hardware.setter
    def hardware(self, hardware):
        """Sets the hardware of this ExperimentSpecSerializer.


        :param hardware: The hardware of this ExperimentSpecSerializer.
        :type hardware: str
        """
        if hardware is None:
            raise ValueError("Invalid value for `hardware`, must not be `None`")  # noqa: E501

        self._hardware = hardware

    @property
    def params(self):
        """Gets the params of this ExperimentSpecSerializer.


        :return: The params of this ExperimentSpecSerializer.
        :rtype: List[ExperimentSpecParamsSerializer]
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ExperimentSpecSerializer.


        :param params: The params of this ExperimentSpecSerializer.
        :type params: List[ExperimentSpecParamsSerializer]
        """

        self._params = params

    @property
    def datasets(self):
        """Gets the datasets of this ExperimentSpecSerializer.


        :return: The datasets of this ExperimentSpecSerializer.
        :rtype: List[WorkspaceSpecDatasetsSerializer]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this ExperimentSpecSerializer.


        :param datasets: The datasets of this ExperimentSpecSerializer.
        :type datasets: List[WorkspaceSpecDatasetsSerializer]
        """

        self._datasets = datasets
