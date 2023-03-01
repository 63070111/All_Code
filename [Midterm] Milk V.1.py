"""[Midterm] Milk V.1"""
def milk():
    """ราคานมต่อขวด"""
    price = int(input())
    pay = int(input())
    free = int(input())
    money = int(input())
    bottle = money//price
    total = bottle
    if pay == 0 and free == 0:
        total = total
    else:
        while True:
            bonus = (bottle//pay)*free
            total += bonus
            left = bottle-((bottle//pay)*pay)
            bottle = bonus+left
            if bottle < pay:
                break
    print(total)
milk()

