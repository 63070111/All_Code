"""diamond"""
def mond():
    """รูปเพชร"""
    number = int(input())
    half = number//2
    for gup in range(number):
        for glow in range(number):
            if glow == half - gup or glow == half + gup or gup == half or \
                    glow == gup - half or glow == number - gup + half - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
mond()
