"""Matrix_MN"""
def number():
    """รันเลข"""
    nix = []
    one = int(input())
    two = int(input())
    for _ in range(one*two):
        save = int(input())
        nix.append(save)
    time = 0
    for _ in range(one):
        for _ in range(two):
            print(nix[time], end=" ")
            time += 1
        print()
number()
