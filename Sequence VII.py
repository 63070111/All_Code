"""Sequence VII"""
def number():
    """เลข"""
    num = int(input())
    for i in range(num-1):
        for j in range(i+1):
            print(j+1, end=" ")
        print()

    for i in range(num):
        print(i+1, end=" ")
    print()

    for i in range(num-1):
        for j in range(num-i-1):
            print(j+1, end=" ")
        print()
number()
