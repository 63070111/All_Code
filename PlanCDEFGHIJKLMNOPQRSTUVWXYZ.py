"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def word(name, num1, num2, num3):
    """Plan"""
    if name == "Ascend" and num1 <= num2 <= num3:
        print("%.2f, %.2f, %.2f" % (num1, num2, num3))
    elif name == "Ascend" and num1 <= num3 <= num2:
        print("%.2f, %.2f, %.2f" % (num1, num3, num2))
    elif name == "Ascend" and num2 <= num1 <= num3:
        print("%.2f, %.2f, %.2f" % (num2, num1, num3))
    elif name == "Ascend" and num2 <= num3 <= num1:
        print("%.2f, %.2f, %.2f" % (num2, num3, num1))
    elif name == "Ascend" and num3 <= num1 <= num2:
        print("%.2f, %.2f, %.2f" % (num3, num1, num2))
    elif name == "Ascend" and num3 <= num2 <= num1:
        print("%.2f, %.2f, %.2f" % (num3, num2, num1))

    if name == "Descend" and num1 >= num2 >= num3:
        print("%.2f, %.2f, %.2f" % (num1, num2, num3))
    elif name == "Descend" and num1 >= num3 >= num2:
        print("%.2f, %.2f, %.2f" % (num1, num3, num2))
    elif name == "Descend" and num2 >= num1 >= num3:
        print("%.2f, %.2f, %.2f" % (num2, num1, num3))
    elif name == "Descend" and num2 >= num3 >= num1:
        print("%.2f, %.2f, %.2f" % (num2, num3, num1))
    elif name == "Descend" and num3 >= num1 >= num2:
        print("%.2f, %.2f, %.2f" % (num3, num1, num2))
    elif name == "Descend" and num3 >= num2 >= num1:
        print("%.2f, %.2f, %.2f" % (num3, num2, num1))
word(input(), float(input()), float(input()), float(input()))
