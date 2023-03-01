"""rolling bingo!"""
def main():
    """"bingo"""
    bingo = (input())
    bingo1 = (input())
    bingo2 = (input())
    if bingo == bingo1 == bingo2 == "RED":
        print("GiftVoucher")
        return ()
    if bingo == bingo1 == bingo2 == "BLUE":
        print("DoraemonDoll")
        return ()
    if bingo == bingo1 == bingo2 == "GREEN":
        print("FruitBasketBoxset")
        return ()
    if bingo == bingo1 == bingo2 == "GOLD":
        print("NintendoSwitch")
        return ()
    if bingo == bingo1 or \
            bingo1 == bingo2 \
            or bingo2 == bingo:
        print("NoodleCups")
        return()
    else:
        print("TissueBox")
main()





