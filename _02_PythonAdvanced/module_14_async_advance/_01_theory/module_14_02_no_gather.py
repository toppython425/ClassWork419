import asyncio
from datetime import datetime


async def task1():
    await asyncio.sleep(3)
    return 'Task1 result'


async def task2():
    await asyncio.sleep(2)
    return 'Task2 result'


async def main():
    result1 = await task1()
    result2 = await task2()
    print([result1, result2])


if __name__ == '__main__':
    print(datetime.now())
    asyncio.run(main())
    print(datetime.now())
