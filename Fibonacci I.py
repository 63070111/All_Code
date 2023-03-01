"""Fibonacci I"""
def main():
    """Fibonacci"""
    number = int(input())
    number1 = 0
    number2 = 1
    for _ in range(number-1):
        number3 = number2 + number1
        number1 = number2
        number2 = number3
    if number == 0:
        print("0")
    else:
        print(number2)
main()
