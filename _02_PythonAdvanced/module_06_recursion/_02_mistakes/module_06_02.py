# def factorial_rec(n):
#     if n == 1:  # базовый случай
#         return 1
#     return n * factorial_rec(n - 1)
#
#
# print(factorial_rec(1000))
import sys
sys.setrecursionlimit(1001)

def factorial_rec(n):
    if n == 1:  # базовый случай
        return 1
    return n * factorial_rec(n - 1)


print(factorial_rec(1000))
