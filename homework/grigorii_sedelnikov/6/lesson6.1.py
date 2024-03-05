def task_1(string_input):
    part_string = string_input.split(" ")
    result = ""
    for word in part_string:
        if word[-1] in [",", "."]:
            symbol = word[-1]
            word = word[:-1] + "ing" + symbol + " "
            result = result + word
        else:
            result = result + word + "ing" + " "
    print(result)


task_1(
    'Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at, '
    'dignissim vitae libero')
