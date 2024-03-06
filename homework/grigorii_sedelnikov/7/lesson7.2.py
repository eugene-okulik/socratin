words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}


def print_need_count(dictionary):
    for pair in dictionary.items():
        i = 0
        string_result = ''
        while i < pair[1]:
            string_result = string_result + pair[0]
            i += 1
        print(string_result)


print_need_count(words)
