"""emordnilap"""
def main():
    """palindrome"""
    num = input()
    number = int(num)
    nim = number
    nom = 0
    while number > 0:
        nom = (nom * 10) + number % 10
        number //= 10
    if nim == nom:
        print(nim, "is palindrome.")
    else:
        print(nim, "is not palindrome.")
main()
