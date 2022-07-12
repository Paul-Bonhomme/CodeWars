def func(lst: list) -> tuple:
    result = sum(lst[::2])
    result_two = sum(lst[1::2])

    return result, result_two


print(func([100, 68, 77, 100]))