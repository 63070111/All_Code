"""[Midterm] RuleofThree"""
def chosse():
    """เลือกของราคาถูก"""
    sell = int(input())
    total = 0
    costnew = 0
    weight = 0
    for _ in range(sell):
        cost = float(input())
        avg = float(input())
        check = avg/cost
        if check > total:
            total = check
            costnew = cost
            weight = avg
        elif check == total and costnew > cost:
            total = check
            costnew = cost
            weight = avg
    print("%.2f %.2f" % (costnew, weight))
chosse()
