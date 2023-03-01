"""PickThemAgain"""
def line():
    """เรียง"""
    number = input().split(" ")
    nix = []
    for i in number:
        if int(i) % 3 == 0 or int(i) % 5 == 0:
            nix.append(i)
    nix.reverse()
    if len(nix) == 0:
        print("Nope")
    else:
        for j in nix:
            print(j)
line()
