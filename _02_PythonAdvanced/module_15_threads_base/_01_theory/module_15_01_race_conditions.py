import threading


def increment():
    global counter
    for _ in range(100000):
        counter += 1


if __name__ == '__main__':
    counter = 0
    # Создаём потоки
    threads = []
    # threads = [threading.Thread(target=increment) for i in range(5)]
    for i in range(5):
        threads.append(threading.Thread(target=increment))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(counter)
