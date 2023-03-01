"""WordSequence II"""
def tops():
    """ตามทฤษฎี"""
    one = input()
    two = input()
    nix = [one]
    top = max(len(one), len(two))
    total = 1
    for i in range(0, top):
        stop = one[total:]
        three = two[0:i+1]
        totals = three+stop
        nix.append(totals)
        total += 1
    for j in nix:
        print(j, end='\n')
tops()
