from multiprocessing import Process, Queue, shared_memory
import array
import time


# Функция для вычисления квадрата числа и записи результата в разделяемую память
def compute_square(shm_name, index, queue):
    # Подключаемся к разделяемой памяти
    shm = shared_memory.SharedMemory(name=shm_name)

    # Создаём массив на основе разделяемой памяти
    shared_array = array.array('i', shm.buf)  # 'i' означает int

    # Вычисляем квадрат числа по индексу
    num = shared_array[index]
    result = num ** 2
    shared_array[index] = result

    # Отправляем результат в очередь для дополнительной проверки
    queue.put((index, result))

    # Закрываем доступ к разделяемой памяти
    shm.close()

    # Имитация задержки
    time.sleep(1)


if __name__ == "__main__":
    # Исходные данные: список целых чисел
    data = array.array('i', [1, 2, 3])  # Массив целых чисел

    # Создаём разделяемую память
    shm = shared_memory.SharedMemory(create=True, size=data.buffer_info()[1] * data.itemsize)

    # Копируем данные в разделяемую память
    shared_array = array.array('i', shm.buf)
    shared_array[:] = data[:]

    # Создаём очередь для обмена результатами
    queue = Queue()

    # Создаём и запускаем процессы
    processes = []
    for i in range(len(data)):
        process = Process(target=compute_square, args=(shm.name, i, queue))
        processes.append(process)
        process.start()

    # Ожидаем завершения всех процессов
    for process in processes:
        process.join()

    # Чтение результатов из очереди
    print("\nРезультаты, полученные из очереди:")
    while not queue.empty():
        index, result = queue.get()
        print(f"Индекс {index}, квадрат = {result}")

    # Чтение итогового массива из разделяемой памяти
    print("\nИтоговый массив в разделяемой памяти:")
    shared_array = array.array('i', shm.buf)  # Обновляем ссылку на массив
    print(shared_array.tolist())  # Преобразуем в список для вывода

    # Освобождаем ресурсы разделяемой памяти
    shm.close()
    shm.unlink()

    print("Все процессы завершены.")
