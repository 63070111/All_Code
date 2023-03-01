"""Save"""
def safe():
    """รหัสลับ"""
    one = input()
    two = input()
    pon = 0
    for i in range(len(one)):
        if one[i] == two[i]:
            pass
        else:
            top = total(one[i])
            tip = total(two[i])
            maxs = max(top, tip)
            num = (26-maxs)+(top+tip-maxs)
            nim = abs(tip-top)
            sim = min(num, nim)
            pon += sim
    print(pon)
def total(run):
    """แทนค่า"""
    nat = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9,
           'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17,
           'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    pat = nat[run]
    return pat
safe()
