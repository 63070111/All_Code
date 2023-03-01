"""[Final] Compound Interest"""
def interest(money, tax, year):
    """คิดดอกเบี้ย"""
    money1 = money
    for _ in range(1, year+1):
        total = money1 * (tax/100)
        money1 += total
    print('%.2f' %(money1))
interest(int(input()), float(input()), int(input()))
