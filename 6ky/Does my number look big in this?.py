def narcissistic(value):
    value = str(value)
    size = len(value)
    summa = 0
    for el in value:
        summa += int(el) ** size
    return summa == int(value)



print(narcissistic(153))
print(narcissistic(7))
print(narcissistic(10))
print(narcissistic(15))





