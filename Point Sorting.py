"""Point Sorting"""
def point():
    """จุดบนระนาบ"""
    for _ in range(int(input())):
        total = []
        for _ in range(int(input())):
            word = input().split()
            total.append([int(word[0]), int(word[1])])
        total.sort(key=lambda x: (x[0]+x[1], -x[1]))
        for i in total:
            print(*i)
point()

