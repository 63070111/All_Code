"""BookWorm"""
def book():
    """หนอนหนังสือ"""
    for _ in range(int(input())):
        time = int(input())
        total = 0
        read = [int(input()) for _ in range(int(input()))]
        read.sort()
        for nix in read:
            time -= nix
            if time >= 0:
                total += 1
        print(total)
book()
