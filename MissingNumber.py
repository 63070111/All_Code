"""MissingNumber"""
def line():
    """เอาตัวเลชที่เหลือมา"""
    number = int(input())
    nix = []
    nix2 = list(range(1, number+1))
    for _ in range(number):
        value = int(input())
        if value == 0:
            break
        nix.append(value)
    for j in nix:
        if j in nix2:
            nix2.remove(j)
    nix2.sort()
    for j in nix2:
        print(j)
line()
