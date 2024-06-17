import asyncio
import logging

from app.context import AppContext
from app.server import Server


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    AppContext.init_logging()
    asyncio.run(Server.run(), debug=True)
