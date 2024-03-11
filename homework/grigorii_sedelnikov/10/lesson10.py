# Задание 1
def finish_my(func):
    def wrapper(*args):
        func(*args)
        print("finished")

    return wrapper


@finish_my
def example(text):
    print(text)


example("print me")


# Задание 2
def repeat_me(func):
    def wrapper(*args, count=1):
        i = 0
        while i < count:
            func(*args)
            i = i + 1
        print("finished")

    return wrapper


@repeat_me
def example1(text):
    print(text)


example1("print me", count=5)


# Задание 3
input_1_number = int(input("Введите первое число: "))
input_2_number = int(input("Введите второе число: "))


def decorator(func):
    def wrapper(a, b):
        if a == b:
            return func(a, b, '+')
        elif a < 0 or b < 0:
            return func(a, b, '*')
        elif a > b:
            return func(a, b, '-')
        elif a < b:
            return func(a, b, '/')

    return wrapper


@decorator
def calc(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '/':
        return a / b
    elif operation == '*':
        return a * b


print(calc(input_1_number, input_2_number))

# List comprehension
PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

PRICE_LIST = [x.split() for x in PRICE_LIST.split('\n')]
PRICE_LIST_DICT = {x[0]: int(str(x[1]).replace('р', '')) for x in PRICE_LIST}
print(PRICE_LIST_DICT)
