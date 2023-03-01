"""Sequence IX"""
def line(number):
    """พีรามิด"""
    for i in range(number):
        for j in range(number-i-1):
            print(" "*2, end=" ")

        for j in range(i+1):
            print(str(j+1).zfill(2), end=" ")

        for j in range(i):
            print(str(i-j).zfill(2), end=" ")
        print()
line(int(input()))
