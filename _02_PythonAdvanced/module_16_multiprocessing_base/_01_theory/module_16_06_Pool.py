from multiprocessing import Pool


def square(x):
    return x ** 2


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        numbers = [1, 2, 3, 4, 5, 6, 7, 8]

        results = pool.map(square, numbers)
    print(f'Квадраты чисел: {results}')
