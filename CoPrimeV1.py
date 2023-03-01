"""CoPrimeV1"""
def number(one, two):
    """ห.ร.ม"""
    first_max = max(one, two)
    second_min = min(one, two)
    nix = []
    for i in range(1, second_min+1):
        if first_max % i == 0 and second_min % i == 0:
            nix.append(i)
        else:
            pass
    nix.sort()
    if len(nix) == 1:
        print("YES")
        print(nix[-1])
    else:
        print("NO")
        print(nix[-1])
number(int(input()), int(input()))

