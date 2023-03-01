"""BusStop I"""
def buss():
    """รอรถ"""
    human = int(input())
    bus = int(input())
    nix = []
    total = 0
    run = [input().split() for i in range(bus)]
    run.sort(key=lambda x: int(x[0]))
    for data in run:
        data = [int(j) for j in data]
        home = data[0]
        total += nix.count(home)
        nix = list(filter(lambda x, s=home: x != s, nix))
        nom = human - len(nix)
        data = list(filter(lambda x, s=home, m=bus: m >= x > s, data))
        data = data[0:nom]
        nix.extend(data)
    print(total)
buss()
