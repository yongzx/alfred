# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: query.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()

DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x0bquery.proto\x12\x05unary\"9\n\x11\x44\x61taHeaderRequest\x12\x11\n\tdata_meta\x18\x01 \x01(\t\x12\x11\n\tdata_size\x18\x02 \x01(\x04\":\n\x12\x44\x61taHeaderResponse\x12\x11\n\tdata_meta\x18\x01 \x01(\t\x12\x11\n\tdata_size\x18\x02 \x01(\x04\"D\n\x0f\x44\x61taReadySignal\x12\x11\n\tdata_size\x18\x01 \x01(\x04\x12\x13\n\x06kwargs\x18\x02 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_kwargs\"V\n\x10InferenceRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\tcandidate\x18\x02 \x01(\t\x12\x13\n\x06kwargs\x18\x03 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_kwargs\"f\n\rEncodeRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x11\n\timmediate\x18\x02 \x01(\x08\x12\x11\n\treduction\x18\x03 \x01(\t\x12\x13\n\x06kwargs\x18\x04 \x01(\tH\x00\x88\x01\x01\x42\t\n\x07_kwargs\"4\n\x0e\x45ncodeResponse\x12\x11\n\tembedding\x18\x01 \x01(\x0c\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x89\x01\n\x11InferenceResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x0e\n\x06ranked\x18\x02 \x01(\x08\x12\x0f\n\x07success\x18\x03 \x01(\x08\x12\x12\n\x05logit\x18\x04 \x01(\tH\x00\x88\x01\x01\x12\x16\n\tembedding\x18\x05 \x01(\x0cH\x01\x88\x01\x01\x42\x08\n\x06_logitB\x0c\n\n_embedding2\x99\x02\n\x0cQueryService\x12@\n\tInference\x12\x17.unary.InferenceRequest\x1a\x18.unary.InferenceResponse\"\x00\x12?\n\x06\x45ncode\x12\x17.unary.InferenceRequest\x1a\x18.unary.InferenceResponse\"\x00\x30\x01\x12\x41\n\tDataReady\x12\x16.unary.DataReadySignal\x1a\x18.unary.InferenceResponse\"\x00\x30\x01\x12\x43\n\nDataHeader\x12\x18.unary.DataHeaderRequest\x1a\x19.unary.DataHeaderResponse\"\x00\x62\x06proto3'
)

_DATAHEADERREQUEST = DESCRIPTOR.message_types_by_name['DataHeaderRequest']
_DATAHEADERRESPONSE = DESCRIPTOR.message_types_by_name['DataHeaderResponse']
_DATAREADYSIGNAL = DESCRIPTOR.message_types_by_name['DataReadySignal']
_INFERENCEREQUEST = DESCRIPTOR.message_types_by_name['InferenceRequest']
_ENCODEREQUEST = DESCRIPTOR.message_types_by_name['EncodeRequest']
_ENCODERESPONSE = DESCRIPTOR.message_types_by_name['EncodeResponse']
_INFERENCERESPONSE = DESCRIPTOR.message_types_by_name['InferenceResponse']
DataHeaderRequest = _reflection.GeneratedProtocolMessageType(
    'DataHeaderRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _DATAHEADERREQUEST,
        '__module__': 'query_pb2'
        # @@protoc_insertion_point(class_scope:unary.DataHeaderRequest)
    })
_sym_db.RegisterMessage(DataHeaderRequest)

DataHeaderResponse = _reflection.GeneratedProtocolMessageType(
    'DataHeaderResponse',
    (_message.Message, ),
    {
        'DESCRIPTOR': _DATAHEADERRESPONSE,
        '__module__': 'query_pb2'
        # @@protoc_insertion_point(class_scope:unary.DataHeaderResponse)
    })
_sym_db.RegisterMessage(DataHeaderResponse)

DataReadySignal = _reflection.GeneratedProtocolMessageType(
    'DataReadySignal',
    (_message.Message, ),
    {
        'DESCRIPTOR': _DATAREADYSIGNAL,
        '__module__': 'query_pb2'
        # @@protoc_insertion_point(class_scope:unary.DataReadySignal)
    })
_sym_db.RegisterMessage(DataReadySignal)

InferenceRequest = _reflection.GeneratedProtocolMessageType(
    'InferenceRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _INFERENCEREQUEST,
        '__module__': 'query_pb2'
        # @@protoc_insertion_point(class_scope:unary.InferenceRequest)
    })
_sym_db.RegisterMessage(InferenceRequest)

EncodeRequest = _reflection.GeneratedProtocolMessageType(
    'EncodeRequest',
    (_message.Message, ),
    {
        'DESCRIPTOR': _ENCODEREQUEST,
        '__module__': 'query_pb2'
        # @@protoc_insertion_point(class_scope:unary.EncodeRequest)
    })
_sym_db.RegisterMessage(EncodeRequest)

EncodeResponse = _reflection.GeneratedProtocolMessageType(
    'EncodeResponse',
    (_message.Message, ),
    {
        'DESCRIPTOR': _ENCODERESPONSE,
        '__module__': 'query_pb2'
        # @@protoc_insertion_point(class_scope:unary.EncodeResponse)
    })
_sym_db.RegisterMessage(EncodeResponse)

InferenceResponse = _reflection.GeneratedProtocolMessageType(
    'InferenceResponse',
    (_message.Message, ),
    {
        'DESCRIPTOR': _INFERENCERESPONSE,
        '__module__': 'query_pb2'
        # @@protoc_insertion_point(class_scope:unary.InferenceResponse)
    })
_sym_db.RegisterMessage(InferenceResponse)

_QUERYSERVICE = DESCRIPTOR.services_by_name['QueryService']
if _descriptor._USE_C_DESCRIPTORS == False:

    DESCRIPTOR._options = None
    _DATAHEADERREQUEST._serialized_start = 22
    _DATAHEADERREQUEST._serialized_end = 79
    _DATAHEADERRESPONSE._serialized_start = 81
    _DATAHEADERRESPONSE._serialized_end = 139
    _DATAREADYSIGNAL._serialized_start = 141
    _DATAREADYSIGNAL._serialized_end = 209
    _INFERENCEREQUEST._serialized_start = 211
    _INFERENCEREQUEST._serialized_end = 297
    _ENCODEREQUEST._serialized_start = 299
    _ENCODEREQUEST._serialized_end = 401
    _ENCODERESPONSE._serialized_start = 403
    _ENCODERESPONSE._serialized_end = 455
    _INFERENCERESPONSE._serialized_start = 458
    _INFERENCERESPONSE._serialized_end = 595
    _QUERYSERVICE._serialized_start = 598
    _QUERYSERVICE._serialized_end = 879
# @@protoc_insertion_point(module_scope)
