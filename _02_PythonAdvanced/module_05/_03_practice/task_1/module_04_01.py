def count_unique(numbers: list[int]) -> dict[int, int]:
    """
    Возвращает количество встречающихся элементов списка
    :param numbers: (list[int]) - список целых чисел
    :return: (dict[int, int]) - словарь ключ - сам элемент, значение - сколько раз он встретился в списке
    """

    counter = dict()
    print(counter)
    for item in numbers:
        if item not in counter:
            counter[item] = 0
        counter[item] += 1
    return counter


if __name__ == '__main__':
    print(count_unique([1, 1, 1, 2, 3, 5, 4, 5, 6, 4, 8, 5, 4, 5]))

# 1:0 - 1я итерация строка 12
# 1:1 - 1я итерация строка 13
# 1:2 - 2я итерация строка 13
# 1:3 - 3я итерация строка 13
# 2:0 - 4я итерация строка 12
# 2:1 - 4я итерация строка 13
