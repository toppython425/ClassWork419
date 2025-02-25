import random
import asyncio


async def fetch_data(api_id):
    print(f'Запрос к API {api_id} начат...')
    await asyncio.sleep(random.randint(2, 4))
    print(f'Запрос к API {api_id} завершен.')
    return f'Данные API: {api_id}'


async def main():
    result1 = await fetch_data(1)
    result2 = await fetch_data(2)
    result3 = await fetch_data(3)
    print(f'Все запросы выполнены:')
    print(f'Результаты:', [result1, result2, result3])


if __name__ == '__main__':
    asyncio.run(main())
