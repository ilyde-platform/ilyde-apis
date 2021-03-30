# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apis_server.serializers.base_model_ import Model
from apis_server.serializers.file_serializer import FileSerializer
from apis_server import util


class DatasetVersionSerializer(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, dataset=None, name=None, author=None, related_bucket=None, bucket_tree=None, size=None, create_at=None):  # noqa: E501
        """DatasetVersionSerializer - a model defined in OpenAPI

        :param id: The id of this DatasetVersionSerializer.  # noqa: E501
        :type id: str
        :param dataset: The dataset of this DatasetVersionSerializer.  # noqa: E501
        :type dataset: str
        :param name: The name of this DatasetVersionSerializer.  # noqa: E501
        :type name: str
        :param author: The author of this DatasetVersionSerializer.  # noqa: E501
        :type author: str
        :param related_bucket: The related_bucket of this DatasetVersionSerializer.  # noqa: E501
        :type related_bucket: str
        :param bucket_tree: The bucket_tree of this DatasetVersionSerializer.  # noqa: E501
        :type bucket_tree: List[FileSerializer]
        :param size: The size of this DatasetVersionSerializer.  # noqa: E501
        :type size: int
        :param create_at: The create_at of this DatasetVersionSerializer.  # noqa: E501
        :type create_at: str
        """
        self.openapi_types = {
            'id': str,
            'dataset': str,
            'name': str,
            'author': str,
            'related_bucket': str,
            'bucket_tree': List[FileSerializer],
            'size': int,
            'create_at': str
        }

        self.attribute_map = {
            'id': 'id',
            'dataset': 'dataset',
            'name': 'name',
            'author': 'author',
            'related_bucket': 'related_bucket',
            'bucket_tree': 'bucket_tree',
            'size': 'size',
            'create_at': 'create_at'
        }

        self._id = id
        self._dataset = dataset
        self._name = name
        self._author = author
        self._related_bucket = related_bucket
        self._bucket_tree = bucket_tree
        self._size = size
        self._create_at = create_at

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The DatasetVersion of this DatasetVersionSerializer.  # noqa: E501
        :rtype: DatasetVersionSerializer
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this DatasetVersionSerializer.


        :return: The id of this DatasetVersionSerializer.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DatasetVersionSerializer.


        :param id: The id of this DatasetVersionSerializer.
        :type id: str
        """

        self._id = id

    @property
    def dataset(self):
        """Gets the dataset of this DatasetVersionSerializer.


        :return: The dataset of this DatasetVersionSerializer.
        :rtype: str
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this DatasetVersionSerializer.


        :param dataset: The dataset of this DatasetVersionSerializer.
        :type dataset: str
        """

        self._dataset = dataset

    @property
    def name(self):
        """Gets the name of this DatasetVersionSerializer.


        :return: The name of this DatasetVersionSerializer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasetVersionSerializer.


        :param name: The name of this DatasetVersionSerializer.
        :type name: str
        """

        self._name = name

    @property
    def author(self):
        """Gets the author of this DatasetVersionSerializer.


        :return: The author of this DatasetVersionSerializer.
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this DatasetVersionSerializer.


        :param author: The author of this DatasetVersionSerializer.
        :type author: str
        """

        self._author = author

    @property
    def related_bucket(self):
        """Gets the related_bucket of this DatasetVersionSerializer.


        :return: The related_bucket of this DatasetVersionSerializer.
        :rtype: str
        """
        return self._related_bucket

    @related_bucket.setter
    def related_bucket(self, related_bucket):
        """Sets the related_bucket of this DatasetVersionSerializer.


        :param related_bucket: The related_bucket of this DatasetVersionSerializer.
        :type related_bucket: str
        """

        self._related_bucket = related_bucket

    @property
    def bucket_tree(self):
        """Gets the bucket_tree of this DatasetVersionSerializer.


        :return: The bucket_tree of this DatasetVersionSerializer.
        :rtype: List[FileSerializer]
        """
        return self._bucket_tree

    @bucket_tree.setter
    def bucket_tree(self, bucket_tree):
        """Sets the bucket_tree of this DatasetVersionSerializer.


        :param bucket_tree: The bucket_tree of this DatasetVersionSerializer.
        :type bucket_tree: List[FileSerializer]
        """

        self._bucket_tree = bucket_tree

    @property
    def size(self):
        """Gets the size of this DatasetVersionSerializer.


        :return: The size of this DatasetVersionSerializer.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this DatasetVersionSerializer.


        :param size: The size of this DatasetVersionSerializer.
        :type size: int
        """

        self._size = size

    @property
    def create_at(self):
        """Gets the create_at of this DatasetVersionSerializer.


        :return: The create_at of this DatasetVersionSerializer.
        :rtype: str
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        """Sets the create_at of this DatasetVersionSerializer.


        :param create_at: The create_at of this DatasetVersionSerializer.
        :type create_at: str
        """

        self._create_at = create_at
