a = int(input("Введи число 1:"))
b = int(input("Введи число 2:"))


def add(y, x):
    return x + y


def multiply(x, y):
    return x * y


def subtraction(x, y):
    return x - y


print("Сумма: ", add(a, b))
print("Разность: ", subtraction(a, b))
print("Умножение: ", multiply(a, b))
