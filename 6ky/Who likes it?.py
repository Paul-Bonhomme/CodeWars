
def likes(lst):
    if len(lst) == 0:
        print("no one like this.")
    elif len(lst) == 1:
        print(f"{lst[0]} likes this")
    elif len(lst) == 2:
        print(f"{lst[0]} and {lst[1]} likes this")
    elif len(lst) == 3:
        print(f"{lst[0]}, {lst[1]} and {lst[2]} likes this")
    else:
        print(f"{lst[0]}, {lst[1]} and {len(lst[2::])} others like this")

