"""[Midterm] Diginity"""
def number():
    """คิดเลข"""
    space = []
    while True:
        digit = input()
        if int(digit) == 0:
            break
        else:
            one = 0
            two = 0
            three = 0
            four = 0
            for i in digit:
                one += int(i)
            for j in str(one):
                two += int(j)
            for tol in str(two):
                three += int(tol)
            for jol in str(three):
                four += int(jol)
            space.append(four)
    for total in space:
        print(total, end="\n")
number()

