import time
from multiprocessing import Process


def long_task():
    print("Процесс начал работу.")
    time.sleep(10)
    print("Процесс завершил работу.")


if __name__ == '__main__':
    process = Process(target=long_task)
    process.start()

    time.sleep(4)
    if process.is_alive():
        print(f'Процесс все еще работает. Прерываем его.')
        process.terminate()

    process.join()
    print("Процесс завершен.")
