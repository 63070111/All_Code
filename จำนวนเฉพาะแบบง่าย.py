""" prime """
def number():
    """เฉพาะ"""
    value = int(input())
    total = 0
    for i in range(1, value + 1):
        if value % i == 0:
            total += i
    if total == value + 1:
        print("Yes")
    else:
        print("No")
number()
