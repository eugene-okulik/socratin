import math

x = int(input("Введи катет 1: "))
y = int(input("Введи катет 2: "))

def square(a, b):
    return (a + b) / 2

def gypotinuze(a, b):
    result = math.sqrt(a*a + b*b)
    return round(result, 2)



print(square(x, y))
print(gypotinuze(x, y))