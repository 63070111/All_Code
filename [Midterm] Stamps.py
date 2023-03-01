"""[Midterm] Stamps"""
def stamp(term, price, cumulative, star, discount):
    """stamp"""
    total = 0
    beyond = 0
    for _ in range(term):
        bill = int(input())
        if total > 0 and total >= star:
            need = bill//discount
            if bill % discount != 0:
                need += 1
            use = total//star
            if use >= need:
                bill = 0
                total -= need*star
            else:
                bill -= use*discount
                bill = max(bill, 0)
                total -= use*star
        if bill >= price:
            collect = bill//price
            total += collect*cumulative
        beyond += bill
    print(beyond)
    print(total)
stamp(int(input()), int(input()), int(input()), int(input()), int(input()))
