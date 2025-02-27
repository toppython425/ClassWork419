import threading
import time


def send_request(server, delay):
    print(f'Запрос к серверу {server} начался ...')
    time.sleep(delay)
    print(f'Запрос к серверу {server} завершен!')


def simulate_requests():
    servers = [("Server1", 2), ("Server2", 1), ("Server3", 3)]
    threads = []
    for server, delay in servers:
        thread = threading.Thread(target=send_request, args=(server, delay))
        threads.append(thread)

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


if __name__ == '__main__':
    simulate_requests()
