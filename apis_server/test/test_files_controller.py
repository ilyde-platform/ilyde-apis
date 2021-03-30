# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from apis_server.serializers import ErrorSerializer
from apis_server.test import BaseTestCase


class TestFilesController(BaseTestCase):
    """FilesController integration test stubs"""

    def test_get_experiment_artifact(self):
        """Test case for get_experiment_artifact

        Download experiment artifact
        """
        query_string = [('id', 'id_example'),
                        ('path', 'path_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/experiment-artifacts/download',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_project_file(self):
        """Test case for get_project_file

        Download project's file
        """
        query_string = [('id', 'id_example'),
                        ('path', 'path_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/project-files/download',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
