from multiprocessing import Process, Queue


# def task():
#     print(f'Процесс начал работу.')
#     result = 1 / 0
#     print(f'Процесс завершен')
#
#
# if __name__ == '__main__':
#     process = Process(target=task)
#     process.start()
#     process.join()
#     print("Основной процесс завершен")


def task(divider, queue):
    try:
        print("Процесс начал работу")
        result = 10 / divider
        print(result)
    except Exception as e:  # ZeroDivisionError
        queue.put(str(e))


if __name__ == '__main__':
    queue = Queue()
    process1 = Process(target=task, args=(0, queue))
    process2 = Process(target=task, args=(5, queue))
    process1.start()
    process2.start()

    process_counter = 1
    for process in [process1, process2]:
        process.join()
        if not queue.empty():
            error_message = queue.get()
            print(f'Ошибка в процессе {process_counter}: {error_message}')
        else:
            print(f'Процесс {process_counter} завершился успешно')
        process_counter += 1
