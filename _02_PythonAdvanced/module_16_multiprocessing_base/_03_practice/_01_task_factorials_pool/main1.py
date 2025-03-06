from multiprocessing import Pool
import math


def compute_factorial(n):
    return math.factorial(n)


if __name__ == '__main__':
    numbers = [number for number in range(1, 101)]
    with Pool(processes=4) as pool:
        results = pool.map(compute_factorial, numbers)

    for n, result in zip(numbers, results):
        print(f'Факториал {n}: {result}')
