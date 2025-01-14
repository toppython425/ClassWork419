my_set = {1, 2, (3, 4)}
print(my_set)

# my_set_1 = {1, 2, [3, 4]}
# print(my_set)


math_students = {'Alice', 'Bob', 'Charlie'}
physics_students = {'Bob', 'Dave', 'Eve'}

both_courses = math_students & physics_students
print("Both courses", both_courses)

only_math = math_students - physics_students
print("Only math", only_math)

any_course = math_students | physics_students
print('Any course', any_course)