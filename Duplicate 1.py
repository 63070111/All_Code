"""Duplicate 1"""
def line(one, two):
    """1"""
    three = set()
    four = set()
    for _ in range(one):
        value1 = int(input())
        three.add(value1)
    for _ in range(two):
        value2 = int(input())
        four.add(value2)
    five = sorted(three.intersection(four), reverse=True)
    if five == []:
        print('Nope')
    else:
        for i in five:
            print(i, sep='\n')
line(int(input()), int(input()))

