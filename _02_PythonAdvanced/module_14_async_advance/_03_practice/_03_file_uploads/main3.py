import asyncio
from datetime import datetime


async def upload_file(file_name, delay):
    print(f'Начало загрузки файла {file_name}...')
    await asyncio.sleep(delay)
    print(f'{file_name} успешно загружен!')
    return file_name


async def monitor_file_uploads(files):
    # tasks = [asyncio.create_task(upload_file(file, delay)) for file, delay in files]

    tasks = []
    for file_name, delay in files:
        tasks.append(asyncio.create_task(upload_file(file_name, delay)))

    while any(not task.done() for task in tasks):
        # completed = [task.result() for task in tasks if task.done()]
        completed = []
        for task in tasks:
            if task.done():
                completed.append(task.result())
        print(f'Загружено файлов: {len(completed)} ({', '.join(completed)})')
        await asyncio.sleep(2)
    # results = [await task for task in tasks]
    results = []
    for task in tasks:
        results.append(await task)
    print("Все файлы успешно загружены", results)


if __name__ == '__main__':
    print(datetime.now())
    my_files = [("file1.txt", 6), ("file2.txt", 4), ("file3.txt", 8)]
    asyncio.run(monitor_file_uploads(my_files))
    print(datetime.now())
