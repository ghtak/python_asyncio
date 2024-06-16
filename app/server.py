import asyncio
from asyncio import StreamReader, StreamWriter

from app.session import Session


class Server:

    @classmethod
    async def handle_client(cls, reader: StreamReader, writer: StreamWriter):
        session = Session(reader, writer)
        await session.handle_event()

    async def run(self):
        server = await asyncio.start_server(
            Server.handle_client,
            '0.0.0.0',
            7544
        )
        print(f'Serving on {server.sockets[0].getsockname()}')
        async with server:
            await server.serve_forever()
