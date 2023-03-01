"""Sequence V"""
def print_loop(num):
    """range"""
    count = 1
    for i in range(num, 0, -1):
        if count > 7:
            print()
            print(i, end=" ")
            count = 2
        else:
            print(i, end=" ")
            count += 1
print_loop(int(input()))
