# def calc_sum(n):
#     res = 0
#     while True:
#         if n == 0:
#             break
#         res += n
#         n -= 1
#     return res
#
#
# print(calc_sum(10))

def calc_sum_recursive(n):
    if n == 1:
        return 1
    return n + calc_sum_recursive(n - 1)


# 10 + calc_sum_recursive(10 - 1) + calc_sum_recursive(9 - 1) + calc_sum_recursive(8 - 1) + ... + calc_sum_recursive(2 - 1)
# 10             9                              8                         7              6 5 4 3 2             1

print(calc_sum_recursive(10))
