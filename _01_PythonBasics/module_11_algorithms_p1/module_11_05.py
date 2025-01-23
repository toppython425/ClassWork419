def find_max(lst):
    max_value = lst[0]
    for num in lst:
        if num > max_value:
            max_value = num
    return max_value


scores_input = input('Введите результаты участников через пробел: ')
scores_list = []
for score in scores_input.split():
    scores_list.append(int(score))
print(f"Результаты участников {scores_list}")
max_score = find_max(scores_list)
print(f'Максимальный результат {max_score}')
