"""OC / DC"""
def main():
    """oc"""
    skill = input()
    level = int(input())
    item_name = input()
    item_price = int(input())
    if skill == 'OC':
        if level == 1:
            new_price = \
                item_price * 1.07
        elif level == 2:
            new_price = \
                item_price * 1.09
        elif level == 3:
            new_price = \
                item_price * 1.11
        elif level == 4:
            new_price = \
                item_price * 1.13
        elif level == 5:
            new_price = \
                item_price * 1.15
        elif level == 6:
            new_price = \
                item_price * 1.17
        elif level == 7:
            new_price = \
                item_price * 1.19
        elif level == 8:
            new_price = \
                item_price * 1.21
        elif level == 9:
            new_price = \
                item_price * 1.23
        else:
            new_price = \
                item_price * 1.24
    else:
        if level == 1:
            new_price = \
                item_price * 0.93
        elif level == 2:
            new_price = \
                item_price * 0.91
        elif level == 3:
            new_price = \
                item_price * 0.89
        elif level == 4:
            new_price = \
                item_price * 0.87
        elif level == 5:
            new_price = \
                item_price * 0.85
        elif level == 6:
            new_price = \
                item_price * 0.83
        elif level == 7:
            new_price = \
                item_price * 0.81
        elif level == 8:
            new_price = \
                item_price * 0.79
        elif level == 9:
            new_price = \
                item_price * 0.77
        else:
            new_price = \
                item_price * 0.76
        if new_price <= 1:
            new_price = 1
    print("[%s LV.%d] %s: %d "
          "z -> %d z" %
          (skill, level, item_name,
           item_price, new_price))
main()




