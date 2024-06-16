import os
import asyncio
import logging


async def coro_func():
    await asyncio.sleep(1, 42)
    print("awaited")


async def main():
    await coro_func()

if __name__ == '__main__':
    os.environ['PYTHONASYNCIODEBUG'] = "1"
    logging.basicConfig(level=logging.DEBUG)
    asyncio.run(main())
