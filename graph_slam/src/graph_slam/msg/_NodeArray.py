"""autogenerated by genpy from graph_slam/NodeArray.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct

import graph_slam.msg

class NodeArray(genpy.Message):
  _md5sum = "4b009d3ef060038e61c7be91101a1af0"
  _type = "graph_slam/NodeArray"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """#Array of nodes returned from the graph slam optimization
Node[] nodes

================================================================================
MSG: graph_slam/Node
float64 x
float64 y
float64 theta


"""
  __slots__ = ['nodes']
  _slot_types = ['graph_slam/Node[]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       nodes

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(NodeArray, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.nodes is None:
        self.nodes = []
    else:
      self.nodes = []

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      length = len(self.nodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.nodes:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.theta))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      if self.nodes is None:
        self.nodes = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.nodes = []
      for i in range(0, length):
        val1 = graph_slam.msg.Node()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _struct_3d.unpack(str[start:end])
        self.nodes.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      length = len(self.nodes)
      buff.write(_struct_I.pack(length))
      for val1 in self.nodes:
        _x = val1
        buff.write(_struct_3d.pack(_x.x, _x.y, _x.theta))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      if self.nodes is None:
        self.nodes = None
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      self.nodes = []
      for i in range(0, length):
        val1 = graph_slam.msg.Node()
        _x = val1
        start = end
        end += 24
        (_x.x, _x.y, _x.theta,) = _struct_3d.unpack(str[start:end])
        self.nodes.append(val1)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_3d = struct.Struct("<3d")
