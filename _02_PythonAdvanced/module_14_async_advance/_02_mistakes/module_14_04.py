import asyncio


# def sync_function():
#     return 42
#
# async def main():
#     await asyncio.gather(sync_function())

def sync_function():
    return 42


async def wrapper():
    return sync_function()


async def main():
    await asyncio.gather(wrapper())


if __name__ == '__main__':
    asyncio.run(main())
