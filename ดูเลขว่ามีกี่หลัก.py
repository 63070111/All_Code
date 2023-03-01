"""How long II"""
def main():
    """หลัก"""
    import math
    number = int(input())
    try:
        digits = int(math.log10(abs(number))) + 1
    except ValueError:
        digits = 1

    print(digits)
main()
