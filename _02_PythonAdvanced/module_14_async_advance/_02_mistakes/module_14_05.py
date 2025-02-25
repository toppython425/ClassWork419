import asyncio


# async def task():
#     await asyncio.sleep(1)
#
#
# async def main():
#     asyncio.gather(task(), task())


async def task():
    await asyncio.sleep(1)


async def main():
    await asyncio.gather(task(), task())


if __name__ == '__main__':
    asyncio.run(main())
