"""Sequence X"""
def line(number):
    """กลับด้าน"""
    for i in range(number):
        for j in range(number-i-1):
            print(" "*2, end=" ")

        amount = 2*i+1
        for j in range(amount):
            factor = int(amount/2)+1
            print(str(abs(abs(factor-j-1)-factor)).zfill(2), end=" ")
        print()

    for i in range(number-1):
        for j in range(i+1):
            print(" "*2, end=" ")

        amount = 2*(number-i-1)-1
        for j in range(amount):
            factor = int(amount/2)+1
            print(str(abs(abs(factor - j - 1) - factor)).zfill(2), end=" ")
        print()
line(int(input()))

