"""[Final] Pro"""
def food(human, buy, price, come):
    """ราคา"""
    num = come % human
    nim = come // human

    if come > human:
        if come % human == 0:
            print((buy*nim) * price)
        else:
            print(((nim*buy)*price)+(num*price))

    elif come == human:
        print(buy * price)

    else:
        print(come * price)

food(int(input()), int(input()), int(input()), int(input()))
