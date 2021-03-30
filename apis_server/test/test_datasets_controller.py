# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from apis_server.serializers.dataset_serializer import DatasetSerializer
from apis_server.serializers.dataset_version_serializer import DatasetVersionSerializer
from apis_server.serializers.error_serializer import ErrorSerializer
from apis_server.serializers.page_limit_list_serializer import PageLimitListSerializer
from apis_server.serializers.status_serializer import StatusSerializer
from apis_server.test import BaseTestCase


class TestDatasetsController(BaseTestCase):
    """DatasetsController integration test stubs"""

    def test_create_dataset(self):
        """Test case for create_dataset

        Create a dataset
        """
        dataset_serializer = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/create',
            method='POST',
            headers=headers,
            data=json.dumps(dataset_serializer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_create_dataset_version(self):
        """Test case for create_dataset_version

        Create dataset's version
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(files=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/v1/dataset-versions/create',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_dataset(self):
        """Test case for delete_dataset

        Delete a dataset
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/delete',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_dataset_versions(self):
        """Test case for list_dataset_versions

        Search for dataset's versions
        """
        inline_object2_serializer = {}
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/dataset-versions/list',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object2_serializer),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_datasets(self):
        """Test case for list_datasets

        List datasets
        """
        inline_object_serializer = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/list',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object_serializer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_dataset(self):
        """Test case for retrieve_dataset

        Retrieve a dataset
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/get',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_dataset(self):
        """Test case for update_dataset

        Update a dataset
        """
        inline_object1_serializer = {}
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/datasets/update',
            method='PATCH',
            headers=headers,
            data=json.dumps(inline_object1_serializer),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
