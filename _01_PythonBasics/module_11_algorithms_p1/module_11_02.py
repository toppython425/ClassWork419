def bubble_sort(lst):
    lst_len = len(lst)
    for i in range(lst_len - 1):
        for j in range(lst_len - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


numbers = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(numbers))
numbers.sort()
print(numbers)

