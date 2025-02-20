import asyncio


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")


async def main():
    task1 = asyncio.create_task(my_coroutine())
    task2 = asyncio.create_task(my_coroutine())
    await task1
    await task2


if __name__ == '__main__':
    asyncio.run(main())
