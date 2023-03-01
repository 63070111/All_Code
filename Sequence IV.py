"""Sequence IV"""
def number(num):
    """Sequence IV"""
    for i in range(1, num **2+1, num):
        for j in range(i, i + num):
            print(j, end=" ")
        print()
number(abs(int(input())))
