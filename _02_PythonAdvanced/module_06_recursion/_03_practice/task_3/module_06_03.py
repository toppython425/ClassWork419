def find_value(tree: list, value):
    if not isinstance(tree, list):
        return tree == value
    for item in tree:
        if find_value(item, value):
            return True
    return False


values_tree = [1, [2, [3, 4], 5], [6, 7]]
input_number = int(input('Введите целое число для поиска: '))
print(find_value(values_tree, input_number))