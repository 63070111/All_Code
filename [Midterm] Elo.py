"""[Midterm] Elo"""
def money(value1, value2, name):
    """[Midterm] Elo"""
    total1 = 1 / (1 + 10 ** ((value2 - value1) / 400))
    total2 = 1 / (1 + 10 ** ((value1 - value2) / 400))
    if name == "A":
        print("%.2f"%(total1))
    elif name == "B":
        print("%.2f"%(total2))
money(float(input()), float(input()), input())
