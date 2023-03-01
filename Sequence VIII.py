"""Sequence VIII"""
def number():
    """เลข"""
    num = int(input())
    for i in range(num):
        k = 1
        for _ in range(num-i-1):
            print(format(" ", "<2"), end=" ")
        for _ in range(i+1):
            print(format("%02d"%(k), "<2"), end=" ")
            k = k+1
        print()

number()
