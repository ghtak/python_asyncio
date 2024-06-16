import asyncio
import logging

from app.server import Server


async def main():
    server = Server()
    await server.run()


if __name__ == '__main__':
    # os.environ['PYTHONASYNCIODEBUG'] = "1"
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main(), debug=True)
