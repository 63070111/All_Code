"""CoinChangev1"""
def money(coin):
    """แลกเงินทอน"""
    number = [25, 10, 5, 1]
    left = 0
    for total in number:
        left = left + coin//total
        coin = coin % total
    return left
print(money(int(input())))

