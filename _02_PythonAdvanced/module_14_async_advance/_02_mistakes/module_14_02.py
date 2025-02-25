import asyncio


# async def task():
#     await asyncio.sleep(1)
#
#
# async def main():
#     tasks = [task(), task(), task()]
#     await asyncio.gather(tasks)


async def task():
    await asyncio.sleep(1)


async def main():
    tasks = [task(), task(), task()]
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    asyncio.run(main())
