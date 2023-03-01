"""Sequence XI"""
def number(num):
    """เรียง"""
    size = num*2-1
    for i in range(1, size+1):
        for j in range(1, size+1):
            print("%02d"%(min(i, j, size-i+1, size-j+1)), end=" ")
        print()
number(int(input()))
