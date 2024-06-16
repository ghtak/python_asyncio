import asyncio
import struct
from unittest.mock import MagicMock

import pytest
import pytest_asyncio

from app.main import read_exactly


@pytest.mark.asyncio
async def test_aio():
    res = await asyncio.sleep(1, result="hello")
    assert "hello" == res


async def mock_read(n):
    return struct.pack('>i', n)


@pytest.mark.asyncio
async def test_mock():
    mock = MagicMock()
    mock.read = mock_read
    res = await read_exactly(mock, 12)
    print(''.join('{:02x}'.format(x) for x in res))
