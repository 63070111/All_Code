"""Regulation"""
def main():
    num1 = str(int(input()))
    num2 = float(input())
    num3 = input()
    print(num1.rjust(30))
    print(num1.rjust(30, "0"))
    print("%.2f" %(num2))
    print("%.12f" %(num2))
    print(num3.rjust(40))
main()
