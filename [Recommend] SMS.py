"""[Recommend] SMS"""
def phone(pot):
    """กดปุ่ม"""
    numbers = ['(DEL)', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PGRS', 'TUV', 'WXYZ']
    nix = []
    for _ in range(pot):
        bottom = int(input())
        number = int(input())
        if bottom == 1:
            if len(nix) >= number:
                for _ in range(number):
                    nix.pop()
            else:
                nix.clear()
        else:
            begin = numbers[bottom-1]
            want = begin[(number-1)%len(begin)]
            nix.append(want)
    if len(nix) > 0:
        for i in nix:
            print(i, end='')
    else:
        print('null')
phone(int(input()))
