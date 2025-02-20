import asyncio


async def process_data(task_id, delay):
    print(f'Задача {task_id} началась...')
    await asyncio.sleep(delay=delay)
    print(f'Задача {task_id} завершена.')
    return f'Результат задачи {task_id}'


async def monitor_task_progress():
    tasks = [
        asyncio.create_task(process_data(1, 6)),
        asyncio.create_task(process_data(2, 4)),
        asyncio.create_task(process_data(3, 12)),
    ]
    while any(not task.done() for task in tasks):
        print("Прогресс: некоторые задачи еще выполняются....")
        await asyncio.sleep(2)

    results = [await task for task in tasks]
    print("Все задачи завершены")
    return results


if __name__ == '__main__':
    asyncio.run(monitor_task_progress())
