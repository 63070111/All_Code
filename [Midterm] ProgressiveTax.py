"""[Midterm] ProgressiveTax"""
def money():
    """คำนวนเงิน"""
    price = int(input())
    total = price
    tax = 0
    if total > 4000000:
        tax += pay((total-4000000), 0.35)
        total = (total-(total-4000000))
    if 2000000 < total <= 4000000:
        tax += pay((total-2000000), 0.3)
        total = (total-(total-2000000))
    if 1000000 < total <= 2000000:
        tax += pay((total-1000000), 0.25)
        total = (total-(total-1000000))
    if 750000 < total <= 1000000:
        tax += pay((total-750000), 0.2)
        total = (total-(total-750000))
    if 500000 < total <= 750000:
        tax += pay((total-500000), 0.15)
        total = (total-(total-500000))
    if 300000 < total <= 500000:
        tax += pay((total-300000), 0.1)
        total = (total-(total-300000))
    if 150000 < total <= 300000:
        tax += pay((total-150000), 0.05)
        total = (total-(total-150000))
    print("%d"%(tax))
def pay(buy, tax1):
    """คิด"""
    change = int(buy*tax1)
    return change
money()
