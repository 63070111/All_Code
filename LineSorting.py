"""LineSorting"""
def line():
    """เรียงบนลงล่าง"""
    one = int(input())
    nix = []
    for _ in range(one):
        word = input()
        nix.append((word))
    nix.sort(key=len)
    for j in nix:
        print(j)
line()

