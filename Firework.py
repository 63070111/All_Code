"""Firework"""
def main():
    """Firework"""
    number = int(input())

    half = int(number / 2)
    for i in range(half):
        for j in range(i):
            print(" ", end="")

        print("\ | /")

    for i in range(half):
        print("-", end="")

    print(" + ", end="")

    for i in range(half):
        print("-", end="")

    print()

    for i in range(half):
        for j in range(half - i - 1):
            print(" ", end="")

        print("/ | \\")
main()
