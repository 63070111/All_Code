"""Sequence I"""
def line(num):
    """Sequence I"""
    for _ in range(1):
        for _ in range(num):
            for num in range(1, num+1):
                print(num, end=" ")
            print()

line(int(input()))
