"""Функция, которая проверяет, вся ли строка с капсом."""


def is_uppercase(inp: str):
    if inp.isupper() == True:
        return True
    else:
        return False

print(is_uppercase("Pasha"))
print(is_uppercase("pasha"))
print(is_uppercase("PASHA"))
