# coding: utf-8

from __future__ import absolute_import
import unittest

from flask import json
from six import BytesIO

from apis_server.test import BaseTestCase


class TestEnvironmentsController(BaseTestCase):
    """EnvironmentsController integration test stubs"""

    def test_create_hardwaretier(self):
        """Test case for create_hardwaretier

        Create HardwareTier
        """
        hardware_tier_serializer = {}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/hardware-tiers/create',
            method='POST',
            headers=headers,
            data=json.dumps(hardware_tier_serializer),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_delete_hardwaretier(self):
        """Test case for delete_hardwaretier

        Delete HardwareTier
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/hardware-tiers/delete',
            method='DELETE',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_environments(self):
        """Test case for list_environments

        List available compute environments
        """
        query_string = [('limit', 26),
                        ('page', 2)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/compute-environments/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_hardwaretiers(self):
        """Test case for list_hardwaretiers

        List available HardwareTiers
        """
        query_string = [('limit', 26),
                        ('page', 2)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/hardware-tiers/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_list_ide(self):
        """Test case for list_ide

        List available Ide for workspaces
        """
        query_string = [('limit', 26),
                        ('page', 2)]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/workspace-ide/list',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_retrieve_hardwaretier(self):
        """Test case for retrieve_hardwaretier

        Retrieve HardwareTier
        """
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/hardware-tiers/get',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_update_hardwaretier(self):
        """Test case for update_hardwaretier

        Update HardwareTier
        """
        hardware_tier_serializer = {}
        query_string = [('id', 'id_example')]
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer special-key',
        }
        response = self.client.open(
            '/api/v1/hardware-tiers/update',
            method='PATCH',
            headers=headers,
            data=json.dumps(hardware_tier_serializer),
            content_type='application/json',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
