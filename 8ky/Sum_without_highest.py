def enough(cap, on, wait):
    return 0 if cap - on - wait >= 0 else abs(cap - on - wait)

print(enough(100, 60, 50))