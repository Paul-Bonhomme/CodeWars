from functools import reduce
from operator import mul

cnt = 0


def persistence(n):
    str_n = str(n)
    lst_n = []

    for el in str_n:
        lst_n.append(int(el))

    global cnt

    result_mul = reduce(mul, lst_n)

    if result_mul >= 10:
        cnt += 1
        return persistence(result_mul)
    else:
        cnt += 1
        return cnt


print(persistence(999))


import operator

def persistence(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i
