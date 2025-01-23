def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1  # index previous
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


grades = input('Введите оценки участников через пробел: ')

grades_list = []
for grade in grades.split():
    grades_list.append(int(grade))
print(f'Исходные оценки {grades_list}')
sorted_grades = insertion_sort(grades_list)
print(f'Отсортированные оценки {sorted_grades}')
# grades_comp = [int(grade) for grade in grades.split()]
