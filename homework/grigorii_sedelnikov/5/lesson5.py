# Задание 1

person = ['John', 'Doe', 'New York', '+1372829383739', 'US']
name, last_name, city, phone, country = person

# Задание 2
string1 = "результат операции: 42"
string2 = "результат операции: 514"
string3 = "результат работы программы: 9"


def return_number_and_add_ten(input_string):
    start_number_index = 2 + input_string.index(":", 0, len(input_string))
    return int(input_string[start_number_index: len(input_string)]) + 10


print(return_number_and_add_ten(string1))
print(return_number_and_add_ten(string2))
print(return_number_and_add_ten(string3))

# Задание 3
students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

print(
    f"Students {students[0]}, {students[1]}, {students[2]} study these subjects: {subjects[0]}, {subjects[1]}, {subjects[2]}")
