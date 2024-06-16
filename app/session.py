import struct
from asyncio import StreamReader, StreamWriter

from app.dto import Header


class Session:
    reader: StreamReader
    writer: StreamWriter

    def __init__(self, reader: StreamReader, writer: StreamWriter):
        self.reader = reader
        self.writer = writer

    async def read_exactly(self, n: int) -> bytes:
        data = bytearray(n)
        wr = 0
        while wr < n:
            ret = await self.reader.read(n - wr)
            rd_size = len(ret)
            if rd_size == 0:
                raise EOFError
            data[wr: wr + rd_size] = ret[:]
            wr += rd_size
        return data

    async def handle_event(self):
        while True:
            try:
                header = await self.read_exactly(12)
                hdr = Header(*struct.unpack('>iii', header))
                body = await self.read_exactly(hdr.size)
            except EOFError:
                pass
