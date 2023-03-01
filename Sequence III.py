"""Sequence III"""
def box(num):
    """Sequence III"""
    for i in range(2, num+2):
        for j in range(i, i+num):
            print(j, end=" ")
        print()
box(int(input()))
