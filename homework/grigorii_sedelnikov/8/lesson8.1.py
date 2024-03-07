import sys
sys.set_int_max_str_digits(100000000)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


count = 1
for number in fibonacci():
    if count == 5:
        print(number)
    if count == 200:
        print(number)
    if count == 1000:
        print(number)
    if count == 100000:
        print(number)
        break
    count += 1
