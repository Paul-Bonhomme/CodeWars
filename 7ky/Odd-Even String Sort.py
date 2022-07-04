"""Given a string s. You have to return another string such that even-indexed and odd-indexed characters of s
are grouped and groups are space-separated (see sample below)

Note:
0 is considered to be an even index.
All input strings are valid with no spaces

Even indices 0, 2, 4, 6, so we have 'CdWr' as the first group
odd ones are 1, 3, 5, 7, so the second group is 'oeas'
And the final string to return is 'Cdwr oeas'"""


#  Мой код

def sorted_my_string(s):
    lst = []
    lst_1 = []

    for el in s:
        if s.index(el) % 2 == 0:
            lst.append(el)
        else:
            lst_1.append(el)

    lst.append(" ")
    lst.extend(lst_1)
    print("".join(lst))


# Код адекватного человека

def sort_my_string(s):
    return s[::2] + ' ' + s[1::2]
