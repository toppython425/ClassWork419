# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# my_gen = my_generator()
# print(type(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))

def count_up_to(limit):
    count = 1
    while count <= limit:
        yield count
        count += 1


for number in count_up_to(10):
    print(number)
