"""Plant"""
def main():
    """Plant"""
    number = int(input())
    if number % 2 == 0 and number % 3 == 0 and 1 <= number <= 30:
        print("Both of them.")
    elif number % 3 == 0 and 1 <= number <= 30:
        print("Bowstring Hemp")
    elif number % 2 == 0 and 1 <= number <= 30:
        print("Cactus")
    elif number % 2 != 0 and number % 3 != 0 and 1 <= number <= 30:
        print("Nothing.")
    else:
        print("Invalid date.")
main()
