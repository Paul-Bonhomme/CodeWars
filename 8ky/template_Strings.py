def temple_string(str1, str2):
    lst = [str1, "are", str2]
    return " ".join(lst)


print(temple_string("Pasha", "Human"))


def new_temple_string(obj, feature):
    return f"{obj} are {feature}"

print(new_temple_string("Pasha", "Human"))

