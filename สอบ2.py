"""La vie en Rose"""
def main():
    """La vie"""
    flower = str(input())
    coin = float(input())
    coin1 = int(input())
    coin2 = float(input())
    num = (len(flower))
    nur = num == coin1 and coin2 * num
    nut = num is not coin1 and coin * num
    print(num, "Rose(s)", "%.2f" %(nur or nut), "Baht")
main()
