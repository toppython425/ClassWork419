from Classes import Student, Classroom

classroom = Classroom()

while True:
    command = input(
        'Введите команду: 1 - добавить студента, 2 - поставить оценку, 3 - вывести список студентов, 0 - выход: '
    )
    if command == '0':
        print('Программа завершена!')
        break
    elif command == '1':
        name = input('Введите имя ученика: ').strip().title()
        student = Student(name)
        classroom.add_student(student)
        print(f'Ученик {name} добавлен.')
    elif command == '2':
        name = input('Введите имя ученика: ').strip().title()
        grade = float(input('Введите оценку: '))
        print(classroom.add_grade_to_student(name, grade))
    elif command == '3':
        classroom.show_students()
    else:
        print('Неизвестная команда, попробуйте снова.')

print(classroom.students)
