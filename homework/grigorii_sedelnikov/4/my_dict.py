my_dict = {"tuple": (1, 2, 3, 4, 5), "list": [3, 0, 4, 5, 6],
           "dict": {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}, "set": {1, 2, 3, 4, 5, 6}}


def first(my_dict):
    count = len(my_dict["tuple"])
    return my_dict["tuple"][count - 1]

def second(my_dict):
    my_list = list(my_dict["list"])
    my_list.pop(1)
    my_list.append(8)
    return my_list

def third(my_dict):
    my_dict = dict(my_dict["dict"])
    my_dict["i am a tuple"] = 777
    del my_dict["two"]
    return my_dict

def fourth(my_dict):
    my_set = set(my_dict["set"])
    my_set.add(6686)
    my_set.remove(1)
    return my_set

def summury(my_dict):
    result = {}
    result["tuple"] = first(my_dict)
    result["list"] = second(my_dict)
    result["dict"] = third(my_dict)
    result["set"] = fourth(my_dict)
    return result

print(summury(my_dict))