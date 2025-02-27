import threading


def add_to_shared_list(item):
    with lock:
        shared_list.append(item)


def worker():
    for i in range(1000):
        add_to_shared_list(i)


if __name__ == '__main__':
    shared_list = []
    lock = threading.Lock()

    threads = [threading.Thread(target=worker) for _ in range(5)]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Ожидаемая длина списка 5000. Фактическая: {len(shared_list)}")
