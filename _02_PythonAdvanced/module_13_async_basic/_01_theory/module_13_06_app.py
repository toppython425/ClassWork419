import asyncio


async def fetch_data(task_id, delay):
    print(f'Task {task_id} started')
    await asyncio.sleep(delay)
    print(f'Task {task_id} finished')
    return f'Data from task {task_id}'


async def main():
    tasks = [
        fetch_data(1, 2),
        fetch_data(2, 1),
        fetch_data(3, 3)
    ]

    results = await asyncio.gather(*tasks)
    print('All tasks finished')
    print('Results:', results)


if __name__ == '__main__':
    asyncio.run(main())
