from _class_task_pool import ThreadPool
from _process_task import process_task

if __name__ == '__main__':
    pool = ThreadPool(3)
    for i in range(10):
        pool.add_task(process_task, i)
