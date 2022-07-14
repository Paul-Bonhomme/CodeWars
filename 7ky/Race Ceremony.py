def race_podium(blocks):
    if blocks == 7:
        return 2, 4, 1
    a, b = divmod(blocks, 3)
    if b == 0:
        return a, a + 1, a - 1
    elif b == 1:
        return a + 1, a + 2, a - 2
    else:
        return a + 1, a + 2, a - 1


print(race_podium(11))
print(race_podium(7))
print(race_podium(9))