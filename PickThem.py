"""PickThem"""
def value():
    """คู่คี่"""
    number = (input())
    import json
    total = json.loads(number)
    nix = []
    for i in total:
        if i % 2 == 0:
            nix.append(i)
        else:
            pass
    nom = len(nix)
    if nom == 0:
        print("Nope")
    else:
        for j in nix:
            print(j)
value()
