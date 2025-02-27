import threading
import queue
import time


def worker(q):
    while not q.empty():
        task = q.get()
        print(f'Выполняю задачу: {task} ')
        time.sleep(1)
        q.task_done()


if __name__ == '__main__':
    q = queue.Queue()
    for i in range(6):
        q.put(f'Задача: {i}')

    threads = [threading.Thread(target=worker, args=(q,)) for i in range(3)]

    for thread in threads:
        thread.start()

    q.join()
    print("Все задачи завершены.")
