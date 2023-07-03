# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import policestation_pb2 as policestation__pb2


class policestationServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Police_station = channel.unary_unary(
                '/policestation.policestationService/Police_station',
                request_serializer=policestation__pb2.PolicestationRequest.SerializeToString,
                response_deserializer=policestation__pb2.PolicestationResponse.FromString,
                )
        self.InsertCharges = channel.unary_unary(
                '/policestation.policestationService/InsertCharges',
                request_serializer=policestation__pb2.InsertChargesRequest.SerializeToString,
                response_deserializer=policestation__pb2.InsertChargesResponse.FromString,
                )
        self.DeleteCharges = channel.unary_unary(
                '/policestation.policestationService/DeleteCharges',
                request_serializer=policestation__pb2.DeleteChargesRequest.SerializeToString,
                response_deserializer=policestation__pb2.DeleteChargesResponse.FromString,
                )
        self.FetchNTSA = channel.unary_unary(
                '/policestation.policestationService/FetchNTSA',
                request_serializer=policestation__pb2.FetchNTSARequest.SerializeToString,
                response_deserializer=policestation__pb2.FetchNTSAResponse.FromString,
                )
        self.FetchCharges = channel.unary_unary(
                '/policestation.policestationService/FetchCharges',
                request_serializer=policestation__pb2.FetchchargesRequest.SerializeToString,
                response_deserializer=policestation__pb2.FetchchargesResponse.FromString,
                )


class policestationServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Police_station(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def InsertCharges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteCharges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchNTSA(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FetchCharges(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_policestationServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Police_station': grpc.unary_unary_rpc_method_handler(
                    servicer.Police_station,
                    request_deserializer=policestation__pb2.PolicestationRequest.FromString,
                    response_serializer=policestation__pb2.PolicestationResponse.SerializeToString,
            ),
            'InsertCharges': grpc.unary_unary_rpc_method_handler(
                    servicer.InsertCharges,
                    request_deserializer=policestation__pb2.InsertChargesRequest.FromString,
                    response_serializer=policestation__pb2.InsertChargesResponse.SerializeToString,
            ),
            'DeleteCharges': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteCharges,
                    request_deserializer=policestation__pb2.DeleteChargesRequest.FromString,
                    response_serializer=policestation__pb2.DeleteChargesResponse.SerializeToString,
            ),
            'FetchNTSA': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchNTSA,
                    request_deserializer=policestation__pb2.FetchNTSARequest.FromString,
                    response_serializer=policestation__pb2.FetchNTSAResponse.SerializeToString,
            ),
            'FetchCharges': grpc.unary_unary_rpc_method_handler(
                    servicer.FetchCharges,
                    request_deserializer=policestation__pb2.FetchchargesRequest.FromString,
                    response_serializer=policestation__pb2.FetchchargesResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'policestation.policestationService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class policestationService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Police_station(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/policestation.policestationService/Police_station',
            policestation__pb2.PolicestationRequest.SerializeToString,
            policestation__pb2.PolicestationResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def InsertCharges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/policestation.policestationService/InsertCharges',
            policestation__pb2.InsertChargesRequest.SerializeToString,
            policestation__pb2.InsertChargesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteCharges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/policestation.policestationService/DeleteCharges',
            policestation__pb2.DeleteChargesRequest.SerializeToString,
            policestation__pb2.DeleteChargesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchNTSA(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/policestation.policestationService/FetchNTSA',
            policestation__pb2.FetchNTSARequest.SerializeToString,
            policestation__pb2.FetchNTSAResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FetchCharges(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/policestation.policestationService/FetchCharges',
            policestation__pb2.FetchchargesRequest.SerializeToString,
            policestation__pb2.FetchchargesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
