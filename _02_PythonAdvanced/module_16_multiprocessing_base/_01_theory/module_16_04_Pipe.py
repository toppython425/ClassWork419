import time
from multiprocessing import Process, Pipe


def sender(conn):
    for i in range(5):
        print(f"Отправитель отправляет: {i}")
        conn.send(i)
        time.sleep(1)


def receiver(conn):
    while True:
        data = conn.recv()
        if data == "DONE":
            print(f'Получена команда "DONE" процесс приема прерван!')
            break
        print(f'Получатель принял: {data}')


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    sender_process = Process(target=sender, args=(parent_conn,))
    receiver_process = Process(target=receiver, args=(child_conn,))

    sender_process.start()
    receiver_process.start()

    sender_process.join()
    parent_conn.send("DONE")
    receiver_process.join()

    print("Обмен данными завершен.")
