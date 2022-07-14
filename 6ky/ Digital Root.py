def digital_root(num):
    num = str(num)
    new_num = list(num)
    lst_new = []

    for el in new_num:
        lst_new.append(int(el))

    result_sum = sum(lst_new)

    if result_sum >= 10:
        return digital_root(result_sum)
    else:
        return result_sum


print(digital_root(493193))