a = int(input("Введи число 1:"))
b = int(input("Введи число 2:"))

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtraction(a, b):
    return a - b


print("Сумма: ", add(a, b))
print("Разность: ", subtraction(a, b))
print("Умножение: ", multiply(a, b))
