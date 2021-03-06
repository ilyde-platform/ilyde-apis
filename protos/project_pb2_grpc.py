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

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from protos import project_pb2 as project__pb2


class ProjectServicesStub(object):
    """The project service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Retrieve = channel.unary_unary(
                '/project.ProjectServices/Retrieve',
                request_serializer=project__pb2.ID.SerializeToString,
                response_deserializer=project__pb2.Project.FromString,
                )
        self.Create = channel.unary_unary(
                '/project.ProjectServices/Create',
                request_serializer=project__pb2.Project.SerializeToString,
                response_deserializer=project__pb2.Project.FromString,
                )
        self.Update = channel.unary_unary(
                '/project.ProjectServices/Update',
                request_serializer=project__pb2.Project.SerializeToString,
                response_deserializer=project__pb2.Project.FromString,
                )
        self.Delete = channel.unary_unary(
                '/project.ProjectServices/Delete',
                request_serializer=project__pb2.ID.SerializeToString,
                response_deserializer=project__pb2.Status.FromString,
                )
        self.Search = channel.unary_unary(
                '/project.ProjectServices/Search',
                request_serializer=project__pb2.SearchProjectRequest.SerializeToString,
                response_deserializer=project__pb2.SearchProjectResponse.FromString,
                )
        self.RetrieveRevision = channel.unary_unary(
                '/project.ProjectServices/RetrieveRevision',
                request_serializer=project__pb2.ID.SerializeToString,
                response_deserializer=project__pb2.Revision.FromString,
                )
        self.CreateRevision = channel.unary_unary(
                '/project.ProjectServices/CreateRevision',
                request_serializer=project__pb2.Revision.SerializeToString,
                response_deserializer=project__pb2.Revision.FromString,
                )
        self.SearchRevision = channel.unary_unary(
                '/project.ProjectServices/SearchRevision',
                request_serializer=project__pb2.SearchRevisionRequest.SerializeToString,
                response_deserializer=project__pb2.SearchRevisionResponse.FromString,
                )


class ProjectServicesServicer(object):
    """The project service definition.
    """

    def Retrieve(self, request, context):
        """Retrieve a project from id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Create(self, request, context):
        """Create a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Update(self, request, context):
        """Update a project
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Delete a project from ID
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Search(self, request, context):
        """Search for projects
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RetrieveRevision(self, request, context):
        """Retrieve a project's revision from id
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateRevision(self, request, context):
        """Create a project's Revision
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchRevision(self, request, context):
        """Search for project's revisions
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ProjectServicesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Retrieve': grpc.unary_unary_rpc_method_handler(
                    servicer.Retrieve,
                    request_deserializer=project__pb2.ID.FromString,
                    response_serializer=project__pb2.Project.SerializeToString,
            ),
            'Create': grpc.unary_unary_rpc_method_handler(
                    servicer.Create,
                    request_deserializer=project__pb2.Project.FromString,
                    response_serializer=project__pb2.Project.SerializeToString,
            ),
            'Update': grpc.unary_unary_rpc_method_handler(
                    servicer.Update,
                    request_deserializer=project__pb2.Project.FromString,
                    response_serializer=project__pb2.Project.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=project__pb2.ID.FromString,
                    response_serializer=project__pb2.Status.SerializeToString,
            ),
            'Search': grpc.unary_unary_rpc_method_handler(
                    servicer.Search,
                    request_deserializer=project__pb2.SearchProjectRequest.FromString,
                    response_serializer=project__pb2.SearchProjectResponse.SerializeToString,
            ),
            'RetrieveRevision': grpc.unary_unary_rpc_method_handler(
                    servicer.RetrieveRevision,
                    request_deserializer=project__pb2.ID.FromString,
                    response_serializer=project__pb2.Revision.SerializeToString,
            ),
            'CreateRevision': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateRevision,
                    request_deserializer=project__pb2.Revision.FromString,
                    response_serializer=project__pb2.Revision.SerializeToString,
            ),
            'SearchRevision': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchRevision,
                    request_deserializer=project__pb2.SearchRevisionRequest.FromString,
                    response_serializer=project__pb2.SearchRevisionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'project.ProjectServices', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ProjectServices(object):
    """The project service definition.
    """

    @staticmethod
    def Retrieve(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/Retrieve',
            project__pb2.ID.SerializeToString,
            project__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Create(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/Create',
            project__pb2.Project.SerializeToString,
            project__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Update(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/Update',
            project__pb2.Project.SerializeToString,
            project__pb2.Project.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/Delete',
            project__pb2.ID.SerializeToString,
            project__pb2.Status.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Search(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/Search',
            project__pb2.SearchProjectRequest.SerializeToString,
            project__pb2.SearchProjectResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RetrieveRevision(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/RetrieveRevision',
            project__pb2.ID.SerializeToString,
            project__pb2.Revision.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateRevision(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/CreateRevision',
            project__pb2.Revision.SerializeToString,
            project__pb2.Revision.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchRevision(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/project.ProjectServices/SearchRevision',
            project__pb2.SearchRevisionRequest.SerializeToString,
            project__pb2.SearchRevisionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
