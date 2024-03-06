def return_number_and_add_ten(input_string):
    start_number_index = 2 + input_string.index(":", 0, len(input_string))
    return int(input_string[start_number_index: len(input_string)]) + 10


def get_number_array(array_string):
    for item in array_string:
        print(return_number_and_add_ten(item))


string1 = "результат операции: 42"
string2 = "результат операции: 54"
string3 = "результат работы программы: 209"
string4 = "результат: 2"

array_answer = [string1, string2, string3, string4]

print(get_number_array(array_answer))
