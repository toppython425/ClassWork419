def max_depth(structure: list) -> int:
    # если структура не список, то глубина равна 0
    if not isinstance(structure, list):
        return 0

    # если список пуст, то глубина равна 1
    if not structure:
        return 1

    # Рекурсивный случай: вычисляем глубину для каждого элемента списка.
    return 1 + max(max_depth(item) for item in structure)


my_structure = [1, [2, [3, [4]]], [5]]
print(max_depth(my_structure))
