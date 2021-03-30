# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: project.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='project.proto',
  package='project',
  syntax='proto3',
  serialized_options=b'\n\026org.hopenly.ilyde.grpcB\014ProjectProtoP\001\242\002\002PS',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rproject.proto\x12\x07project\",\n\x0b\x46ileVersion\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\t\"\x10\n\x02ID\x12\n\n\x02id\x18\x01 \x01(\t\"\x82\x02\n\x07Project\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\'\n\nvisibility\x18\x04 \x01(\x0e\x32\x13.project.VISIBILITY\x12#\n\x08template\x18\x05 \x01(\x0e\x32\x11.project.TEMPLATE\x12\r\n\x05owner\x18\x06 \x01(\t\x12\x0f\n\x07members\x18\x07 \x03(\t\x12\x1d\n\x05state\x18\x08 \x01(\x0e\x32\x0e.project.STATE\x12\x13\n\x0brepo_bucket\x18\t \x01(\t\x12\x11\n\tcreate_at\x18\n \x01(\t\x12\x13\n\x0blast_update\x18\x0b \x01(\t\"\x83\x01\n\x08Revision\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06\x63ommit\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\x0f\n\x07project\x18\x04 \x01(\t\x12\'\n\tfile_tree\x18\x05 \x03(\x0b\x32\x14.project.FileVersion\x12\x11\n\tcreate_at\x18\x06 \x01(\t\")\n\x06Status\x12\x0e\n\x06status\x18\x01 \x01(\r\x12\x0f\n\x07message\x18\x02 \x01(\t\"\x98\x02\n\x14SearchProjectRequest\x12:\n\x05query\x18\x01 \x01(\x0b\x32+.project.SearchProjectRequest.ProjectFilter\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\r\n\x05limit\x18\x03 \x01(\r\x1a\xa6\x01\n\rProjectFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\'\n\nvisibility\x18\x03 \x01(\x0e\x32\x13.project.VISIBILITY\x12#\n\x08template\x18\x04 \x01(\x0e\x32\x11.project.TEMPLATE\x12\x0e\n\x06member\x18\x05 \x01(\t\x12\x1d\n\x05state\x18\x06 \x01(\x0e\x32\x0e.project.STATE\"\xb1\x01\n\x15SearchRevisionRequest\x12<\n\x05query\x18\x01 \x01(\x0b\x32-.project.SearchRevisionRequest.RevisionFilter\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\r\n\x05limit\x18\x03 \x01(\r\x1a=\n\x0eRevisionFilter\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07project\x18\x02 \x01(\t\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\"c\n\x15SearchProjectResponse\x12\r\n\x05total\x18\x01 \x01(\r\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x1e\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x10.project.Project\"e\n\x16SearchRevisionResponse\x12\r\n\x05total\x18\x01 \x01(\r\x12\x0c\n\x04page\x18\x02 \x01(\r\x12\r\n\x05limit\x18\x03 \x01(\r\x12\x1f\n\x04\x64\x61ta\x18\x04 \x03(\x0b\x32\x11.project.Revision*%\n\nVISIBILITY\x12\x0b\n\x07PRIVATE\x10\x00\x12\n\n\x06PUBLIC\x10\x01*\x1d\n\x05STATE\x12\x08\n\x04OPEN\x10\x00\x12\n\n\x06\x43LOSED\x10\x01*\x17\n\x08TEMPLATE\x12\x0b\n\x07GENERIC\x10\x00\x32\xd8\x03\n\x0fProjectServices\x12+\n\x08Retrieve\x12\x0b.project.ID\x1a\x10.project.Project\"\x00\x12.\n\x06\x43reate\x12\x10.project.Project\x1a\x10.project.Project\"\x00\x12.\n\x06Update\x12\x10.project.Project\x1a\x10.project.Project\"\x00\x12(\n\x06\x44\x65lete\x12\x0b.project.ID\x1a\x0f.project.Status\"\x00\x12I\n\x06Search\x12\x1d.project.SearchProjectRequest\x1a\x1e.project.SearchProjectResponse\"\x00\x12\x34\n\x10RetrieveRevision\x12\x0b.project.ID\x1a\x11.project.Revision\"\x00\x12\x38\n\x0e\x43reateRevision\x12\x11.project.Revision\x1a\x11.project.Revision\"\x00\x12S\n\x0eSearchRevision\x12\x1e.project.SearchRevisionRequest\x1a\x1f.project.SearchRevisionResponse\"\x00\x42-\n\x16org.hopenly.ilyde.grpcB\x0cProjectProtoP\x01\xa2\x02\x02PSb\x06proto3'
)

_VISIBILITY = _descriptor.EnumDescriptor(
  name='VISIBILITY',
  full_name='project.VISIBILITY',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PRIVATE', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='PUBLIC', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1195,
  serialized_end=1232,
)
_sym_db.RegisterEnumDescriptor(_VISIBILITY)

VISIBILITY = enum_type_wrapper.EnumTypeWrapper(_VISIBILITY)
_STATE = _descriptor.EnumDescriptor(
  name='STATE',
  full_name='project.STATE',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OPEN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='CLOSED', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1234,
  serialized_end=1263,
)
_sym_db.RegisterEnumDescriptor(_STATE)

STATE = enum_type_wrapper.EnumTypeWrapper(_STATE)
_TEMPLATE = _descriptor.EnumDescriptor(
  name='TEMPLATE',
  full_name='project.TEMPLATE',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GENERIC', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=1265,
  serialized_end=1288,
)
_sym_db.RegisterEnumDescriptor(_TEMPLATE)

TEMPLATE = enum_type_wrapper.EnumTypeWrapper(_TEMPLATE)
PRIVATE = 0
PUBLIC = 1
OPEN = 0
CLOSED = 1
GENERIC = 0



_FILEVERSION = _descriptor.Descriptor(
  name='FileVersion',
  full_name='project.FileVersion',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='project.FileVersion.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='project.FileVersion.version', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=26,
  serialized_end=70,
)


_ID = _descriptor.Descriptor(
  name='ID',
  full_name='project.ID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='project.ID.id', index=0,
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
  serialized_start=72,
  serialized_end=88,
)


_PROJECT = _descriptor.Descriptor(
  name='Project',
  full_name='project.Project',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='project.Project.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='project.Project.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='description', full_name='project.Project.description', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='project.Project.visibility', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template', full_name='project.Project.template', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='owner', full_name='project.Project.owner', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='members', full_name='project.Project.members', index=6,
      number=7, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='project.Project.state', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='repo_bucket', full_name='project.Project.repo_bucket', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='project.Project.create_at', index=9,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='last_update', full_name='project.Project.last_update', index=10,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=91,
  serialized_end=349,
)


_REVISION = _descriptor.Descriptor(
  name='Revision',
  full_name='project.Revision',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='project.Revision.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='commit', full_name='project.Revision.commit', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='project.Revision.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='project.Revision.project', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='file_tree', full_name='project.Revision.file_tree', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='create_at', full_name='project.Revision.create_at', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=352,
  serialized_end=483,
)


_STATUS = _descriptor.Descriptor(
  name='Status',
  full_name='project.Status',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='project.Status.status', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='project.Status.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=485,
  serialized_end=526,
)


_SEARCHPROJECTREQUEST_PROJECTFILTER = _descriptor.Descriptor(
  name='ProjectFilter',
  full_name='project.SearchProjectRequest.ProjectFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='project.SearchProjectRequest.ProjectFilter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='project.SearchProjectRequest.ProjectFilter.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='visibility', full_name='project.SearchProjectRequest.ProjectFilter.visibility', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='template', full_name='project.SearchProjectRequest.ProjectFilter.template', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='member', full_name='project.SearchProjectRequest.ProjectFilter.member', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='state', full_name='project.SearchProjectRequest.ProjectFilter.state', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=643,
  serialized_end=809,
)

_SEARCHPROJECTREQUEST = _descriptor.Descriptor(
  name='SearchProjectRequest',
  full_name='project.SearchProjectRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='project.SearchProjectRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='project.SearchProjectRequest.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='project.SearchProjectRequest.limit', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHPROJECTREQUEST_PROJECTFILTER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=529,
  serialized_end=809,
)


_SEARCHREVISIONREQUEST_REVISIONFILTER = _descriptor.Descriptor(
  name='RevisionFilter',
  full_name='project.SearchRevisionRequest.RevisionFilter',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='project.SearchRevisionRequest.RevisionFilter.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='project', full_name='project.SearchRevisionRequest.RevisionFilter.project', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='author', full_name='project.SearchRevisionRequest.RevisionFilter.author', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=928,
  serialized_end=989,
)

_SEARCHREVISIONREQUEST = _descriptor.Descriptor(
  name='SearchRevisionRequest',
  full_name='project.SearchRevisionRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='query', full_name='project.SearchRevisionRequest.query', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='project.SearchRevisionRequest.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='project.SearchRevisionRequest.limit', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_SEARCHREVISIONREQUEST_REVISIONFILTER, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=812,
  serialized_end=989,
)


_SEARCHPROJECTRESPONSE = _descriptor.Descriptor(
  name='SearchProjectResponse',
  full_name='project.SearchProjectResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='project.SearchProjectResponse.total', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='project.SearchProjectResponse.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='project.SearchProjectResponse.limit', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='project.SearchProjectResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=991,
  serialized_end=1090,
)


_SEARCHREVISIONRESPONSE = _descriptor.Descriptor(
  name='SearchRevisionResponse',
  full_name='project.SearchRevisionResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='project.SearchRevisionResponse.total', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='page', full_name='project.SearchRevisionResponse.page', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='limit', full_name='project.SearchRevisionResponse.limit', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='data', full_name='project.SearchRevisionResponse.data', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=1092,
  serialized_end=1193,
)

_PROJECT.fields_by_name['visibility'].enum_type = _VISIBILITY
_PROJECT.fields_by_name['template'].enum_type = _TEMPLATE
_PROJECT.fields_by_name['state'].enum_type = _STATE
_REVISION.fields_by_name['file_tree'].message_type = _FILEVERSION
_SEARCHPROJECTREQUEST_PROJECTFILTER.fields_by_name['visibility'].enum_type = _VISIBILITY
_SEARCHPROJECTREQUEST_PROJECTFILTER.fields_by_name['template'].enum_type = _TEMPLATE
_SEARCHPROJECTREQUEST_PROJECTFILTER.fields_by_name['state'].enum_type = _STATE
_SEARCHPROJECTREQUEST_PROJECTFILTER.containing_type = _SEARCHPROJECTREQUEST
_SEARCHPROJECTREQUEST.fields_by_name['query'].message_type = _SEARCHPROJECTREQUEST_PROJECTFILTER
_SEARCHREVISIONREQUEST_REVISIONFILTER.containing_type = _SEARCHREVISIONREQUEST
_SEARCHREVISIONREQUEST.fields_by_name['query'].message_type = _SEARCHREVISIONREQUEST_REVISIONFILTER
_SEARCHPROJECTRESPONSE.fields_by_name['data'].message_type = _PROJECT
_SEARCHREVISIONRESPONSE.fields_by_name['data'].message_type = _REVISION
DESCRIPTOR.message_types_by_name['FileVersion'] = _FILEVERSION
DESCRIPTOR.message_types_by_name['ID'] = _ID
DESCRIPTOR.message_types_by_name['Project'] = _PROJECT
DESCRIPTOR.message_types_by_name['Revision'] = _REVISION
DESCRIPTOR.message_types_by_name['Status'] = _STATUS
DESCRIPTOR.message_types_by_name['SearchProjectRequest'] = _SEARCHPROJECTREQUEST
DESCRIPTOR.message_types_by_name['SearchRevisionRequest'] = _SEARCHREVISIONREQUEST
DESCRIPTOR.message_types_by_name['SearchProjectResponse'] = _SEARCHPROJECTRESPONSE
DESCRIPTOR.message_types_by_name['SearchRevisionResponse'] = _SEARCHREVISIONRESPONSE
DESCRIPTOR.enum_types_by_name['VISIBILITY'] = _VISIBILITY
DESCRIPTOR.enum_types_by_name['STATE'] = _STATE
DESCRIPTOR.enum_types_by_name['TEMPLATE'] = _TEMPLATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FileVersion = _reflection.GeneratedProtocolMessageType('FileVersion', (_message.Message,), {
  'DESCRIPTOR' : _FILEVERSION,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.FileVersion)
  })
_sym_db.RegisterMessage(FileVersion)

ID = _reflection.GeneratedProtocolMessageType('ID', (_message.Message,), {
  'DESCRIPTOR' : _ID,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.ID)
  })
_sym_db.RegisterMessage(ID)

Project = _reflection.GeneratedProtocolMessageType('Project', (_message.Message,), {
  'DESCRIPTOR' : _PROJECT,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.Project)
  })
_sym_db.RegisterMessage(Project)

Revision = _reflection.GeneratedProtocolMessageType('Revision', (_message.Message,), {
  'DESCRIPTOR' : _REVISION,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.Revision)
  })
_sym_db.RegisterMessage(Revision)

Status = _reflection.GeneratedProtocolMessageType('Status', (_message.Message,), {
  'DESCRIPTOR' : _STATUS,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.Status)
  })
_sym_db.RegisterMessage(Status)

SearchProjectRequest = _reflection.GeneratedProtocolMessageType('SearchProjectRequest', (_message.Message,), {

  'ProjectFilter' : _reflection.GeneratedProtocolMessageType('ProjectFilter', (_message.Message,), {
    'DESCRIPTOR' : _SEARCHPROJECTREQUEST_PROJECTFILTER,
    '__module__' : 'project_pb2'
    # @@protoc_insertion_point(class_scope:project.SearchProjectRequest.ProjectFilter)
    })
  ,
  'DESCRIPTOR' : _SEARCHPROJECTREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.SearchProjectRequest)
  })
_sym_db.RegisterMessage(SearchProjectRequest)
_sym_db.RegisterMessage(SearchProjectRequest.ProjectFilter)

SearchRevisionRequest = _reflection.GeneratedProtocolMessageType('SearchRevisionRequest', (_message.Message,), {

  'RevisionFilter' : _reflection.GeneratedProtocolMessageType('RevisionFilter', (_message.Message,), {
    'DESCRIPTOR' : _SEARCHREVISIONREQUEST_REVISIONFILTER,
    '__module__' : 'project_pb2'
    # @@protoc_insertion_point(class_scope:project.SearchRevisionRequest.RevisionFilter)
    })
  ,
  'DESCRIPTOR' : _SEARCHREVISIONREQUEST,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.SearchRevisionRequest)
  })
_sym_db.RegisterMessage(SearchRevisionRequest)
_sym_db.RegisterMessage(SearchRevisionRequest.RevisionFilter)

SearchProjectResponse = _reflection.GeneratedProtocolMessageType('SearchProjectResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHPROJECTRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.SearchProjectResponse)
  })
_sym_db.RegisterMessage(SearchProjectResponse)

SearchRevisionResponse = _reflection.GeneratedProtocolMessageType('SearchRevisionResponse', (_message.Message,), {
  'DESCRIPTOR' : _SEARCHREVISIONRESPONSE,
  '__module__' : 'project_pb2'
  # @@protoc_insertion_point(class_scope:project.SearchRevisionResponse)
  })
_sym_db.RegisterMessage(SearchRevisionResponse)


DESCRIPTOR._options = None

_PROJECTSERVICES = _descriptor.ServiceDescriptor(
  name='ProjectServices',
  full_name='project.ProjectServices',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=1291,
  serialized_end=1763,
  methods=[
  _descriptor.MethodDescriptor(
    name='Retrieve',
    full_name='project.ProjectServices.Retrieve',
    index=0,
    containing_service=None,
    input_type=_ID,
    output_type=_PROJECT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Create',
    full_name='project.ProjectServices.Create',
    index=1,
    containing_service=None,
    input_type=_PROJECT,
    output_type=_PROJECT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Update',
    full_name='project.ProjectServices.Update',
    index=2,
    containing_service=None,
    input_type=_PROJECT,
    output_type=_PROJECT,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Delete',
    full_name='project.ProjectServices.Delete',
    index=3,
    containing_service=None,
    input_type=_ID,
    output_type=_STATUS,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='Search',
    full_name='project.ProjectServices.Search',
    index=4,
    containing_service=None,
    input_type=_SEARCHPROJECTREQUEST,
    output_type=_SEARCHPROJECTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RetrieveRevision',
    full_name='project.ProjectServices.RetrieveRevision',
    index=5,
    containing_service=None,
    input_type=_ID,
    output_type=_REVISION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='CreateRevision',
    full_name='project.ProjectServices.CreateRevision',
    index=6,
    containing_service=None,
    input_type=_REVISION,
    output_type=_REVISION,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='SearchRevision',
    full_name='project.ProjectServices.SearchRevision',
    index=7,
    containing_service=None,
    input_type=_SEARCHREVISIONREQUEST,
    output_type=_SEARCHREVISIONRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PROJECTSERVICES)

DESCRIPTOR.services_by_name['ProjectServices'] = _PROJECTSERVICES

# @@protoc_insertion_point(module_scope)
