"""[Recommend] EuclideanDistance"""
def number():
    """จุดตัด"""
    nix = []
    for _ in range(int(input())):
        nix.append(input().split())
    total = point(nix)
    print('%.2f'%(total))
def point(nix):
    """ติดค่า"""
    num = 0
    for i in range(len(nix)-1):
        pot_x = (int(nix[i+1][0]) - int(nix[i][0]))**2
        pot_y = (int(nix[i+1][1]) - int(nix[i][1]))**2
        num += (pot_x + pot_y)**0.5
    return num
number()
