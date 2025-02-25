import random
import asyncio


async def fetch_data(api_id):
    print(f'Запрос к API {api_id} начат...')
    await asyncio.sleep(random.randint(2, 4))
    print(f'Запрос к API {api_id} завершен.')
    return f'Данные API: {api_id}'


# async def main():
#     """!!!ПЛОХО!!!"""
#     tasks = [fetch_data(i) for i in range(1, 4)]
#     results = await asyncio.gather(tasks)
#     print(f'Все запросы выполнены:', results)


async def main():
    """Правильно"""
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)  # * - означает распаковку списка задач
    print(f'Все запросы выполнены:', results)


if __name__ == '__main__':
    asyncio.run(main())
