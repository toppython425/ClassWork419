def factorial(n):
    if n == 1:  # базовый случай
        return 1


def factorial_rec(n):
    if n == 1:  # базовый случай
        return 1
    return n * factorial_rec(n - 1)



