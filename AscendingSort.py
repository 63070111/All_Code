"""AscendingSort"""
def number():
    """เรียงเลข"""
    nix = [int(input()), int(input()), int(input()), int(input()), int(input())]
    nix.sort()
    for i in range(5):
        print(nix[i])
number()

