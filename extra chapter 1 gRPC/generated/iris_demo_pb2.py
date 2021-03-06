# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: iris_demo.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='iris_demo.proto',
  package='iris',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0firis_demo.proto\x12\x04iris\"j\n\x12IrisPredictRequest\x12\x14\n\x0csepal_length\x18\x01 \x01(\x02\x12\x13\n\x0bsepal_width\x18\x02 \x01(\x02\x12\x14\n\x0cpetal_length\x18\x03 \x01(\x02\x12\x13\n\x0bpetal_width\x18\x04 \x01(\x02\"%\n\x13IrisPredictResponse\x12\x0e\n\x06target\x18\x01 \x01(\t2W\n\x07Predict\x12L\n\x13predict_iris_target\x12\x18.iris.IrisPredictRequest\x1a\x19.iris.IrisPredictResponse\"\x00\x62\x06proto3'
)




_IRISPREDICTREQUEST = _descriptor.Descriptor(
  name='IrisPredictRequest',
  full_name='iris.IrisPredictRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='sepal_length', full_name='iris.IrisPredictRequest.sepal_length', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sepal_width', full_name='iris.IrisPredictRequest.sepal_width', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='petal_length', full_name='iris.IrisPredictRequest.petal_length', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='petal_width', full_name='iris.IrisPredictRequest.petal_width', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=131,
)


_IRISPREDICTRESPONSE = _descriptor.Descriptor(
  name='IrisPredictResponse',
  full_name='iris.IrisPredictResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='iris.IrisPredictResponse.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=133,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['IrisPredictRequest'] = _IRISPREDICTREQUEST
DESCRIPTOR.message_types_by_name['IrisPredictResponse'] = _IRISPREDICTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IrisPredictRequest = _reflection.GeneratedProtocolMessageType('IrisPredictRequest', (_message.Message,), {
  'DESCRIPTOR' : _IRISPREDICTREQUEST,
  '__module__' : 'iris_demo_pb2'
  # @@protoc_insertion_point(class_scope:iris.IrisPredictRequest)
  })
_sym_db.RegisterMessage(IrisPredictRequest)

IrisPredictResponse = _reflection.GeneratedProtocolMessageType('IrisPredictResponse', (_message.Message,), {
  'DESCRIPTOR' : _IRISPREDICTRESPONSE,
  '__module__' : 'iris_demo_pb2'
  # @@protoc_insertion_point(class_scope:iris.IrisPredictResponse)
  })
_sym_db.RegisterMessage(IrisPredictResponse)



_PREDICT = _descriptor.ServiceDescriptor(
  name='Predict',
  full_name='iris.Predict',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=172,
  serialized_end=259,
  methods=[
  _descriptor.MethodDescriptor(
    name='predict_iris_target',
    full_name='iris.Predict.predict_iris_target',
    index=0,
    containing_service=None,
    input_type=_IRISPREDICTREQUEST,
    output_type=_IRISPREDICTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PREDICT)

DESCRIPTOR.services_by_name['Predict'] = _PREDICT

# @@protoc_insertion_point(module_scope)
