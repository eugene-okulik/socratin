my_dict = {"tuple": (1, 2, 3, 4, 5), "list": [3, 0, 4, 5, 6],
           "dict": {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}, "set": {1, 2, 3, 4, 5, 6}}


def first(my_dicts):
    count = len(my_dicts["tuple"])
    return my_dict["tuple"][count - 1]


def second(my_dicts):
    my_list = list(my_dicts["list"])
    my_list.pop(1)
    my_list.append(8)
    return my_list


def third(my_dicts):
    my_new_dict = dict(my_dicts["dict"])
    my_new_dict[('i am a tuple',)] = (7, 7, 7)
    del my_new_dict["two"]
    return my_new_dict


def fourth(my_dicts):
    my_set = set(my_dicts["set"])
    my_set.add(6686)
    my_set.remove(1)
    return my_set


def summury(my_dicts):
    result = {"tuple": first(my_dicts), "list": second(my_dicts), "dict": third(my_dicts), "set": fourth(my_dicts)}
    return result


print(summury(my_dict))
