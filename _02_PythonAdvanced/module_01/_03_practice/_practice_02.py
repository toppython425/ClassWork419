def combine_employee_data(names, positions, salaries):
    combined = zip(names, positions, salaries)
    result = list(map(lambda x: f'{x[0]} - {x[1]}: {x[2]}', combined))
    return result


if __name__ == '__main__':
    names = ["Анна", "Борис", "Виктория"]
    positions = ["Менеджер", "Разработчик", "Аналитик"]
    salaries = [80000, 120000, 90000]
    print(combine_employee_data(names, positions, salaries))
