import asyncio
from datetime import datetime


async def task1():
    await asyncio.sleep(3)
    return 'Task1 result'


async def task2():
    await asyncio.sleep(2)
    return 'Task2 result'


async def main():
    results = await asyncio.gather(task1(), task2())
    print(results)


if __name__ == '__main__':
    print(datetime.now())
    asyncio.run(main())
    print(datetime.now())
