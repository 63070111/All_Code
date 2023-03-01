"""Inflation"""
def pay():
    """เงินเฟ้อ"""
    money = int(float(input())*100)
    years = int(input())
    for _ in range(years):
        money += money*381//10000

    if money == 0:
        print("0.00")
    else:
        money = str(money)
        print(money[:-2]+"."+money[-2:])
pay()



