from multiprocessing import Process, Pool
import time


# def long_task():
#     print("Долгий процесс выполняется")
#     # time.sleep(10)
#     print("Долгий процесс завершен")


# if __name__ == '__main__':
#     processes = []
#     for _ in range(10000):
#         process = Process(target=long_task)
#         processes.append(process)
#         process.start()
#
#     for process in processes:
#         process.join()

def long_task(x):
    print(f"Долгий процесс выполняется для {x}")
    # time.sleep(10)
    print("Долгий процесс для {x} завершен")


if __name__ == '__main__':
    with Pool(4) as pool:
        pool.map(long_task, range(10000))
