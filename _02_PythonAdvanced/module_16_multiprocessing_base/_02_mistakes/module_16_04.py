from multiprocessing import Process


def task():
    print("Процесс выполняется")


# process = Process(target=task)
# process.start()
# process.join()

if __name__ == '__main__':
    process = Process(target=task)
    process.start()
    process.join()
