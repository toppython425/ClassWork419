import time
from multiprocessing import Process, Queue


def compute_square(num, queue):
    result = num ** 2
    print(f'Процесс {num}: вычисление квадрата {num} = {result}')
    queue.put(result)
    time.sleep(2)


if __name__ == '__main__':
    queue = Queue()
    processes = []

    for i in range(1, 4):
        process = Process(target=compute_square, args=(i, queue))
        processes.append(process)
        process.start()

    # for process in processes:
    #     process.start()

    for process in processes:
        process.join()

    print('\nРезультаты вычислений:')
    while not queue.empty():
        result = queue.get()
        print(f'Результат: {result}')

    print(f'Все процессы завершены.')
