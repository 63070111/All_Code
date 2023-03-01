"""Difference"""
def number(one, two):
    """แตกต่าง"""
    nix = set()
    nut = set()
    for _ in range(one):
        num = int(input())
        nix = nix | {num}
    for _ in range(two):
        nim = int(input())
        nut = nut | {nim}
    nip = nix - nut
    nip1 = sorted(nip)
    for i in nip1:
        print(i, end=" ")
number(int(input()), int(input()))
