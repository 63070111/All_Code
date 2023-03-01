"""Citizen card"""
def main():
    """main @@@"""
    number = (input())
    if number.isnumeric():
        number = int(number)
        number1 = number // 10 ** 11
        number2 = (number % 10 ** 11) // 10 ** 10
        number3 = (number % 10 ** 10) // 10 ** 9
        number4 = (number % 10 ** 9) // 10 ** 8
        number5 = (number % 10 ** 8) // 10 ** 7
        number6 = (number % 10 ** 7) // 10 ** 6
        number7 = (number % 10 ** 6) // 10 ** 5
        number8 = (number % 10 ** 5) // 10 ** 4
        number9 = (number % 10 ** 4) // 10 ** 3
        number10 = (number % 10 ** 3) // 10 ** 2
        number11 = (number % 10 ** 2) // 10
        number12 = number % 10
        number13 = (13 * number1 + 12 * number2 + 11 * number3 + 10 * number4 +
                    9 * number5 + 8 * number6 + 7 * number7 + 6 * number8 +
                    5 * number9 + 4 * number10 + 3 * number11 + 2 * number12) % 11
        if number13 <= 1:
            number13 = 1 - number13

        elif number13 > 1:
            number13 = 11 - number13
        print("%013d" % (int(str(number) + str(number13))))
main()










