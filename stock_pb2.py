# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: stock.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)




DESCRIPTOR = _descriptor.FileDescriptor(
  name='stock.proto',
  package='stockmarket',
  serialized_pb='\n\x0bstock.proto\x12\x0bstockmarket\"\xd3\x03\n\x05Stock\x12\x0f\n\x07StockID\x18\x01 \x01(\t\x12\x11\n\tStockName\x18\x02 \x01(\t\x12\x11\n\tStockOpen\x18\x03 \x01(\x02\x12\x16\n\x0eStockNetChange\x18\x04 \x01(\x02\x12\x13\n\x0bStockChange\x18\x05 \x01(\x02\x12\x15\n\rStockDayRange\x18\x06 \x01(\t\x12\x13\n\x0bStockVolume\x18\x07 \x01(\x05\x12\x1a\n\x12StockPreviousClose\x18\x08 \x01(\x02\x12\x16\n\x0eStock52WKRange\x18\t \x01(\t\x12\x16\n\x0eStock1YRReturn\x18\n \x01(\x02\x12\x16\n\x0eStockYTDReturn\x18\x0b \x01(\x02\x12\x15\n\rStockPERation\x18\x0c \x01(\x02\x12\x17\n\x0fStockEarningsPS\x18\r \x01(\x02\x12\x16\n\x0eStockMarketCap\x18\x0e \x01(\x02\x12\x1d\n\x15StockSharesOutdanding\x18\x0f \x01(\x02\x12\x12\n\nStockPrice\x18\x10 \x01(\x02\x12\x15\n\rStockDividend\x18\x11 \x01(\x02\x12\x13\n\x0bStockSector\x18\x12 \x01(\t\x12\x15\n\rStockIndustry\x18\x13 \x01(\t\x12\x18\n\x10StockSubIndustry\x18\x14 \x01(\t\".\n\tStockList\x12!\n\x05stock\x18\x01 \x03(\x0b\x32\x12.stockmarket.Stock')




_STOCK = _descriptor.Descriptor(
  name='Stock',
  full_name='stockmarket.Stock',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='StockID', full_name='stockmarket.Stock.StockID', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockName', full_name='stockmarket.Stock.StockName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockOpen', full_name='stockmarket.Stock.StockOpen', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockNetChange', full_name='stockmarket.Stock.StockNetChange', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockChange', full_name='stockmarket.Stock.StockChange', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockDayRange', full_name='stockmarket.Stock.StockDayRange', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockVolume', full_name='stockmarket.Stock.StockVolume', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockPreviousClose', full_name='stockmarket.Stock.StockPreviousClose', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Stock52WKRange', full_name='stockmarket.Stock.Stock52WKRange', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='Stock1YRReturn', full_name='stockmarket.Stock.Stock1YRReturn', index=9,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockYTDReturn', full_name='stockmarket.Stock.StockYTDReturn', index=10,
      number=11, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockPERation', full_name='stockmarket.Stock.StockPERation', index=11,
      number=12, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockEarningsPS', full_name='stockmarket.Stock.StockEarningsPS', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockMarketCap', full_name='stockmarket.Stock.StockMarketCap', index=13,
      number=14, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockSharesOutdanding', full_name='stockmarket.Stock.StockSharesOutdanding', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockPrice', full_name='stockmarket.Stock.StockPrice', index=15,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockDividend', full_name='stockmarket.Stock.StockDividend', index=16,
      number=17, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockSector', full_name='stockmarket.Stock.StockSector', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockIndustry', full_name='stockmarket.Stock.StockIndustry', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='StockSubIndustry', full_name='stockmarket.Stock.StockSubIndustry', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=29,
  serialized_end=496,
)


_STOCKLIST = _descriptor.Descriptor(
  name='StockList',
  full_name='stockmarket.StockList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='stock', full_name='stockmarket.StockList.stock', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=498,
  serialized_end=544,
)

_STOCKLIST.fields_by_name['stock'].message_type = _STOCK
DESCRIPTOR.message_types_by_name['Stock'] = _STOCK
DESCRIPTOR.message_types_by_name['StockList'] = _STOCKLIST

class Stock(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOCK

  # @@protoc_insertion_point(class_scope:stockmarket.Stock)

class StockList(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _STOCKLIST

  # @@protoc_insertion_point(class_scope:stockmarket.StockList)


# @@protoc_insertion_point(module_scope)