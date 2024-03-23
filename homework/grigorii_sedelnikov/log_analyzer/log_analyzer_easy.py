import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('path_tofile', help='Path to the file')
parser.add_argument("--text", help="Text to search")
args = parser.parse_args()

name_files = []
for file_name in os.listdir(args.path_tofile):
    name_files.append(file_name)

print(name_files)

for file_name in name_files:
    path_to_file = os.path.join(args.path_tofile.replace('\\', '\\'), file_name)
    result_dict_string = {}
    with open(path_to_file, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            result_dict_string[line_number] = line.rstrip('\n')
    for key, value in result_dict_string.items():
        value_dict = value.split(' ')
        if args.text in value_dict:
            index_word_value = value_dict.index(args.text)
            if index_word_value >= 5 and index_word_value + 5 < len(value_dict):
                print(
                    f'Файл: {file_name}, номер строки: {key}, текст ошибки: '
                    f'{" ".join(value_dict[index_word_value - 5:index_word_value + 5])}')
            elif index_word_value < 5:
                print(f'Файл: {file_name}, номер строки: {key}, текст ошибки: '
                      f'{" ".join(value_dict[:index_word_value + 5])}')
            elif index_word_value + 5 >= len(value_dict):
                print(f'Файл: {file_name}, номер строки: {key}, текст ошибки: '
                      f'{" ".join(value_dict[index_word_value - 5:])}')
            elif len(value_dict) >= index_word_value + 5:
                print(
                    f'Файл: {file_name}, номер строки: {key}, текст ошибки: '
                    f'{" ".join(value_dict[index_word_value - 5:index_word_value + 5])}')
