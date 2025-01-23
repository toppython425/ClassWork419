# def my_generator():
#     return 1
#     return 2
#     return 3
#
# print(next(my_generator()))

# def my_generator():
#     yield 1
#     yield 2
#     yield 3
#
#
# my_gen = my_generator()
# print(next(my_gen))
# print(next(my_gen))
# print(next(my_gen))
# print()
#
# my_gen_expression1 = (x * 2 for x in range(5))
# print(list(my_gen_expression1))
# my_gen_expression2 = (x * 2 for x in range(5))
# print(list(my_gen_expression2))
# print()
#
# mygen_expression3 = (x ** 2 for x in range(5))
# print(sum(mygen_expression3))
# print(list(mygen_expression3))
#
# my_gen_expression4 = (x ** 2 for x in range(5))
# result = list(my_gen_expression4)
# print(sum(result))

def infinite_numbers():
    num = 1
    while True:
        yield num * num
        num += 1


# gen = infinite_numbers()
# for n in gen:
#     print(n)

gen = infinite_numbers()
for i in range(10):
    print(next(gen))


def my_simple_gen():
    yield 5
