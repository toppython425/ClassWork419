import asyncio


# async def my_coroutine():
#     print("Start")
#     asyncio.sleep(1)
#     print("End")

async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")
