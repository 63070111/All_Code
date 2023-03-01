"""Sequence XII"""
def box():
    """สร้างกล่อง"""
    number = int(input())
    for i in range(number):
        for j in range(i):
            print(str(number-i+j).zfill(2), end=" ")
        for j in range(number-i):
            print(str(number-j).zfill(2), end=" ")
        for j in range(number-i-1):
            print(str(i+j+2).zfill(2), end=" ")
        for j in range(i):
            print(str(number-j-1).zfill(2), end=" ")
        print()
    for i in range(number-1):
        for j in range(number-i-2):
            print(str(i+j+2).zfill(2), end=" ")
        for j in range(i+2):
            print(str(number-j).zfill(2), end=" ")
        for j in range(i+1):
            print(str(number-i+j).zfill(2), end=" ")
        for j in range(number-i-2):
            print(str(number-j-1).zfill(2), end=" ")
        print()
box()

