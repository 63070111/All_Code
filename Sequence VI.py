"""Sequence VI"""
def line(num):
    """สามเหลี่ยม"""
    for i in range(1, num+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()
line(int(input()))
