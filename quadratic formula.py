"""quadratic formula"""
def main():
    """quadratic formula"""
    number1 = int(input())
    number2 = int(input())
    number3 = int(input())
    if (number2**2) - 4 * (number1 * number3) > 0:
        nom = ((-number2) + ((number2**2 - 4 * number1*number3)**0.5)) / (2*number1)
        nom1 = ((-number2) - ((number2**2 - 4 * number1*number3)**0.5)) / (2*number1)
        print("%.2f" %(nom), "\n""%.2f" %(nom1))
    elif (number2**2) - 4*(number1*number3) == 0:
        nom2 = ((-number2) + ((number2 ** 2 - 4 * number1 * number3) ** 0.5)) / (2 * number1)
        print("%.2f"%(nom2))
    else:
        print("No Answer!")
main()
