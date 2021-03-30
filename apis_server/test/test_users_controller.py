# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from apis_server.serializers.error_serializer_serializer import ErrorSerializer  # noqa: E501
from apis_server.serializers.inline_response2001_serializer_serializer import InlineResponse2001Serializer  # noqa: E501
from apis_server.serializers.page_limit_list_serializer_serializer import PageLimitListSerializer  # noqa: E501
from apis_server.serializers.status_serializer_serializer import StatusSerializer  # noqa: E501
from apis_server.serializers.user_serializer_serializer import UserSerializer  # noqa: E501
from apis_server.test import BaseTestCase


class TestUsersController(BaseTestCase):
    """UsersController integration test stubs"""

    def test_create_user(self):
        """Test case for create_user

        Create a user
        """
        user_serializer = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/users/create',
            method='POST',
            headers=headers,
            data=json.dumps(user_serializer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_user(self):
        """Test case for delete_user

        Delete a user
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/users/delete',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_users(self):
        """Test case for list_users

        list users
        """
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/users/list',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_user(self):
        """Test case for retrieve_user

        Retrieve a user
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/users/get',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_user(self):
        """Test case for update_user

        Update a user
        """
        user_serializer = {}
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/users/update',
            method='PATCH',
            headers=headers,
            data=json.dumps(user_serializer),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
