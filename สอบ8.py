"""Get Digit"""
def main():
    """get"""
    number = abs(float(input()))
    digit = int(input())
    result = int(number % 10 ** digit / 10 ** (digit - 1))
    print(result)
main()
