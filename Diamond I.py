"""Diamond I"""
def diamond():
    """เพชร"""
    one = int(input())
    two = int(input())
    nix = []
    nat = []
    for _ in range(one):
        tubtim = input().split()
        nat.extend(tubtim)
    for i in range(two):
        total = 0
        for j in range(i, len(nat), two):
            total += int(nat[j])
        nix.append(total)
    nix.sort()
    nix.reverse()
    print(nix[0])
diamond()
