try:
    result = 10 / 0
except Exception:
    print("На ноль делить нельзя!")

print("Исключение Exception отработано")
print()


try:
    result = 10 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя!")

print("Исключение ZeroDivisionError отработано")
print()

