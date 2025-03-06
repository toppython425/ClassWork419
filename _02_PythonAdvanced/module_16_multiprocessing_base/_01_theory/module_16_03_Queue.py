import time
from multiprocessing import Process, Queue


def producer(queue):
    for i in range(5):
        print(f"Производитель отправляет: {i}")
        queue.put(i)
        time.sleep(1)


def consumer(queue):
    while True:
        item = queue.get()
        if item == "DONE":
            break
        print(f'Потребитель получил: {item}')


if __name__ == '__main__':
    queue = Queue()

    producer_process = Process(target=producer, args=(queue,))
    consumer_process = Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    queue.put("DONE")

    consumer_process.join()

    print("Обмен данными завершен")
