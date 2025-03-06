from multiprocessing import Process
import time


def task():
    print("Дочерний процесс выполняется")
    time.sleep(5)
    print("Дочерний процесс завершен")


# if __name__ == '__main__':
#     process = Process(target=task)
#     process.start()
#     print('Что то делаем еще')

if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    process.join()
    print('Что то делаем еще')
