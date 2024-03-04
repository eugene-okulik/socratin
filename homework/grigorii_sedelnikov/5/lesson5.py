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

to_string_students = ', '.join(students)
to_string_subjects = ', '.join(subjects)

print(
    f"Students {to_string_students} study these subjects: {to_string_subjects}")
