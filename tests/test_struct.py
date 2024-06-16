import struct
import pytest


def test_struct():
    # big endian
    data = struct.pack('>iii', 1, 2, 3)
    assert data == b'\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00\x03'
    a, b, c = struct.unpack('>iii', data)
    assert a == 1 and b == 2 and c == 3

    # little endian
    data = struct.pack('<iii', 1, 2, 3)
    assert data == b'\x01\x00\x00\x00\x02\x00\x00\x00\x03\x00\x00\x00'
    a, b, c = struct.unpack('<iii', data)
    assert a == 1 and b == 2 and c == 3
