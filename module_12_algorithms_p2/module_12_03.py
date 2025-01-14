def binary_search(lst, target):
    left = 0
    right = len(lst) - 1

    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return f'Индекс искомого элемента: {mid}'
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return f'Элемент не найден!'


sorted_list = [1, 3, 5, 7, 9, 11, 13]

print(binary_search(sorted_list, 15))
