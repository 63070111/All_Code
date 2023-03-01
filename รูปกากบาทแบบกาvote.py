"""Vote Me !!!"""
def main():
    """vote"""
    number = int(input())
    for i in range(number):
        if i == 0 or i == number - 1:
            print("* " * number)
            continue

        for j in range(number):
            if j == 0 or j == number - 1 or i == j or j == number - 1 - i:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        print()
main()
