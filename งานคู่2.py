"""Critical calculator"""
def main():
    """เย้"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    num6 = float(input())
    ctr = (num1/3)+num2
    ctr2 =(num3/3)+num4
    ctr3 = (num5/3)+num6
    print("Critical rate 1 :", "%0.2f" % (ctr), end="%\n")
    print("Critical rate 2 :", "%0.2f" % (ctr2), end="%\n")
    print("Critical rate 3 :", "%0.2f" % (ctr3), end="%\n")
    print("Recommend:", "%.2f" % (max(ctr, ctr2, ctr3)), end="%\n")
    print("Not recommend:", "%.2f" % (min(ctr, ctr2, ctr3)), end="%\n")
main()

