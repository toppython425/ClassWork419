# def factorial_rec(n):
#     return n * factorial_rec(n - 1)
#
#
# print(factorial_rec(10))


def factorial_rec(n):
    if n == 1:  # базовый случай
        return 1
    return n * factorial_rec(n - 1)


print(factorial_rec(10))
