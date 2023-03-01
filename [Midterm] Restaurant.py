""""[Midterm] Restaurant"""
def food():
    """ร้านอาหาร"""
    price = float(input())
    goal = float(input())
    discount = float(input())
    addon = float(input())
    if price + addon >= goal:
        pay1 = (price+addon)*(100-discount)/100
    else:
        pay1 = price+addon
    if price >= goal:
        pay2 = price*(100-discount)/100
    else:
        pay2 = price
    totle = abs(pay1-pay2)
    if pay1 < pay2:
        print("Yes", "%.3f" % (totle))
    elif pay1 > pay2:
        print("No", "%.3f" % (totle))
    else:
        print("Yes")
food()
