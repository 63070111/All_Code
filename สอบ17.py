"""European Trophy"""
def main():
    """วาดรูป"""
    number = int(input())
    for i in range(number):
        print(" " * i, end="")
        print("\\", end="")
        print("#" * ((number - i) * 2 + 1), end="")
        print("/", end="\n\n")

    print(" " * (number), end="")
    print("/#\\", end="\n\n")

    base = int(number / 2) - 1
    for i in range(base):
        print(" " * (number - i - 1), end="")
        print("/", end="")
        print("#" * ((i + 2) * 2 - 1), end="")
        if i == base - 1:
            print("\\")
        else:
            print("\\", end="\n\n")
main()
