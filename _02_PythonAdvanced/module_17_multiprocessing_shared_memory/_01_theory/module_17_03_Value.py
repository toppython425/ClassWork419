from multiprocessing import Value, Process


# shared_value = Value('i', 0)
# print(shared_value.value)
# shared_value.value = 42
# print(shared_value.value)


def increment(shared_value):
    for _ in range(10):
        shared_value.value += 1


if __name__ == '__main__':
    shared_value = Value('i', 0)
    process = Process(target=increment, args=(shared_value,))
    process.start()
    process.join()
    print(f'Итоговое значение: {shared_value.value}')
