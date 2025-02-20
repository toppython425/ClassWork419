import asyncio


async def my_coroutine():
    print("Start")
    await asyncio.sleep(1)
    print("End")
    return 'Done'

async def main():
    task = asyncio.create_task(my_coroutine())
    print(f'Task done: {task.done()}')
    await task
    print(f'Task done: {task.done()}')
    task_result = task.result()
    print(task_result)


if __name__ == '__main__':
    asyncio.run(main())

