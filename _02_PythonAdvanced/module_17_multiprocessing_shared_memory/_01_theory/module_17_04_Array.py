from multiprocessing import Array, Process


# shared_array = Array('i', 5)


def square_elements(shared_array):
    for i in range(len(shared_array)):
        shared_array[i] = shared_array[i] ** 2


if __name__ == '__main__':
    shared_array = Array('i', [1, 2, 3, 4])
    process = Process(target=square_elements, args=(shared_array,))
    process.start()
    process.join()
    print(f'Итоговый массив', list(shared_array))
