# def addition(a: int, b: int) -> int:
#     return a + b
#
#
# print(addition(3, 5))  # 8
# print(addition("3", "5")) # "35"
# print(addition("ab", "cd"))  # "abcd"


def addition(a: int, b: int) -> int:
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError(f'Ожидалось значение a типа int, получено {type(a).__name__}')
    if not isinstance(b, int):
        raise TypeError(f'Ожидалось значение b типа int, получено {type(b).__name__}')
    return a + b


print(addition(3, 5))  # 8
print(addition(3, "5"))  # "35"
print(addition("ab", "cd"))  # "abcd"
