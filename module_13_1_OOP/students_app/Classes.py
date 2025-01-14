class Student:

    def __init__(self, name: str, grades: list = None) -> None:
        self.name = name
        if grades:
            self.grades = grades
        else:
            self.grades = []

    def add_grade(self, grade: float) -> None:
        self.grades.append(grade)

    def average_grade(self) -> float:
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return 0.0


class Classroom:
    def __init__(self) -> None:
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def add_grade_to_student(self, name, grade):
        for student in self.students:
            if student.name == name:
                student.add_grade(grade)
                return f'Оценка {grade}, добавлена для {name}.'
        return f'Ученик с именем {name} не найден!'

    def show_students(self):
        if not self.students:
            print('Список учеников пуст')
        else:
            print('Список учеников')
            for student in self.students:
                print(f'{student.name} - Средний балл: {student.average_grade():.2f}')
