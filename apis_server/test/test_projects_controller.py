# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from apis_server.test import BaseTestCase


class TestProjectsController(BaseTestCase):
    """ProjectsController integration test stubs"""

    def test_create_project(self):
        """Test case for create_project

        Create a project
        """
        project_serializer = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/projects/create',
            method='POST',
            headers=headers,
            data=json.dumps(project_serializer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    @unittest.skip("multipart/form-data not supported by Connexion")
    def test_create_project_revision(self):
        """Test case for create_project_revision

        Create project's revision
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'multipart/form-data',
            'Authorization': 'Bearer special-key',
        }
        data = dict(files=(BytesIO(b'some file data'), 'file.txt'))
        response = self.client.open(
            '/api/v1/project-revisions/create',
            method='POST',
            headers=headers,
            data=data,
            content_type='multipart/form-data',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_project(self):
        """Test case for delete_project

        Delete a project
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/projects/delete',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_project_datasets(self):
        """Test case for list_project_datasets

        List project's datasets
        """
        query_string = [('id', 'id_example'),
                        ('limit', 56),
                        ('page', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/project-datasets/list',
            method='POST',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_project_experiments(self):
        """Test case for list_project_experiments

        Search for project's experiments
        """
        query_string = [('id', 'id_example'),
                        ('limit', 56),
                        ('page', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/project-experiments/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_project_models(self):
        """Test case for list_project_models

        List project's models
        """
        query_string = [('id', 'id_example'),
                        ('limit', 56),
                        ('page', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/project-models/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_project_revisions(self):
        """Test case for list_project_revisions

        List project's revisions
        """
        query_string = [('id', 'id_example'),
                        ('limit', 56),
                        ('page', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/project-revisions/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_project_runs(self):
        """Test case for list_project_runs

        List project's runs
        """
        query_string = [('id', 'id_example'),
                        ('limit', 56),
                        ('page', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/project-runs/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_project_workspaces(self):
        """Test case for list_project_workspaces

        List project's workspaces
        """
        query_string = [('id', 'id_example'),
                        ('limit', 56),
                        ('page', 56)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/project-workspaces/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_projects(self):
        """Test case for list_projects

        List projects
        """
        inline_object8_serializer = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/projects/list',
            method='POST',
            headers=headers,
            data=json.dumps(inline_object8_serializer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_project(self):
        """Test case for retrieve_project

        Retrieve a project
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/projects/get',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_project(self):
        """Test case for update_project

        Update a project
        """
        project_serializer = {}
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/projects/update',
            method='PATCH',
            headers=headers,
            data=json.dumps(project_serializer),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
