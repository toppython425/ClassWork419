import asyncio


# async def faulty_task():
#     raise ValueError('Ошибка в задаче')
#
#
# async def main():
#     await asyncio.gather(faulty_task(), asyncio.sleep(1))

async def faulty_task():
    raise ValueError('Ошибка в задаче')


async def main():
    results = await asyncio.gather(faulty_task(), asyncio.sleep(1), return_exceptions=True)
    print(results[0])


if __name__ == '__main__':
    asyncio.run(main())
