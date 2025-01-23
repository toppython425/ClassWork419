from ClassesEmployee.ClassesEmployee_inheritance_incapsulation import Employee, Manager, Intern

if __name__ == '__main__':
    employees_obj_list = [
        Employee("Иван", "Иванов", 50000),
        Manager("Мария", "Петрова", 80000, 20000),
        Intern("Алексей", "Смирнов", 30000, 0.5)
    ]

    for employee_obj in employees_obj_list:
        print(f'{employee_obj.get_info()} - Зарплата: {employee_obj.get_salary()}')
