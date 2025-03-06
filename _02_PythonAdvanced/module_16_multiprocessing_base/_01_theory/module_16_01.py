from multiprocessing import Process


def say_hello():
    print("Привет от процесса")


if __name__ == '__main__':
    process = Process(target=say_hello)
    process.start()
    process.join()
