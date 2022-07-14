from math import factorial


def func(n: int):
    if n >= 0:
        return factorial(n)


print(func(4))