"""Divide3Or5"""
def number():
    """ผลรวม"""
    num = int(input())
    nix = []
    total = 0
    for i in range(1, num+1):
        if i % 3 == 0 or i % 5 == 0:
            nix.append(i)
    for j in nix:
        total += j
    print(total)

number()
