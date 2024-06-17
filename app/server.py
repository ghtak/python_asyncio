import asyncio
from asyncio import StreamReader, StreamWriter

from app.context import AppContext
from app.session import Session


class Server:

    @classmethod
    async def handle_client(cls, reader: StreamReader, writer: StreamWriter):
        session = Session(reader, writer)
        await session.handle_event()

    @classmethod
    async def run(cls):
        server = await asyncio.start_server(
            Server.handle_client,
            AppContext.config.app_host,
            AppContext.config.app_port
        )
        AppContext.logger.info(f'Serving on {server.sockets[0].getsockname()}')
        async with server:
            await server.serve_forever()
