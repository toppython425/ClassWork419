# def merge_sort(lst):
#     mid = len(lst) // 2
#     left = merge_sort(lst[:mid])
#     right = merge_sort(lst[mid:])
#     return left + right


def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])

    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1

    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])

    return sorted_list


print(merge_sort([1, 3, 5, 2, 4, 6]))
