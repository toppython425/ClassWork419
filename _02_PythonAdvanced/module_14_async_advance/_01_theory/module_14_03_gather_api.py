import random
import asyncio


async def fetch_data(api_id):
    print(f'Запрос к API {api_id} начат...')
    await asyncio.sleep(random.randint(2, 4))
    print(f'Запрос к API {api_id} завершен.')
    return f'Данные API: {api_id}'


async def main():
    tasks = [fetch_data(i) for i in range(1, 4)]
    results = await asyncio.gather(*tasks)
    # tasks_list = []
    # for i in range(1, 4):
    #     tasks_list.append(fetch_data(i))
    # results = await asyncio.gather(*tasks_list)
    print(f'Все запросы выполнены:', results)


if __name__ == '__main__':
    asyncio.run(main())
