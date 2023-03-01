"""[Midterm] Donut"""
def donut(pice_a, pice_b, pice_c, pice_d):
    """Donut"""
    total = pice_b + pice_c
    coin = pice_a * pice_b
    left = pice_d//total
    have = pice_d - (left*total)
    if have >= pice_b:
        left = left + 1
        have = 0
    money = left*coin + have*pice_a
    candy = left*total + have
    print(money, candy)
donut(int(input()), int(input()), int(input()), int(input()))

