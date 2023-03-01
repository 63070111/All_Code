"""Median"""
def number(total):
    """ค่ากลาง"""
    nix = []
    for _ in range(total):
        word = float(input())
        nix.append(word)
    nix.sort()
    value = len(nix)
    if value % 2 == 1:
        one = value//2
        two = nix[one:one+1]
        for j in two:
            print('%.1f'% (j))
    else:
        three = value//2
        four = nix[three-1:three+1]
        sum1 = 0
        for i in four:
            sum1 += int(i)
        print('%.1f'% (sum1/2))
number(int(input()))
