import asyncio
import random

urls = [
    "https://example.com/page1",
    "https://example.com/page2",
    "https://example.com/page3",
    "https://example.com/page4",
    "https://example.com/page5",
]


async def download_page(url):
    """Симулирует загрузку страницы."""
    print(f'Начинаю загрузку {url}')
    await asyncio.sleep(random.uniform(1, 5))
    print(f'Загрузка завершена: {url}')


async def main():
    tasks = []
    for url in urls:
        task = asyncio.create_task(download_page(url))
        tasks.append(task)

    for task in tasks:
        await task


if __name__ == '__main__':
    asyncio.run(main())
