"""emordnilap III"""
def main():
    """Palindromeแบบลบ"""
    number = abs(int(input()))
    palin_number = int(str(number)[::-1])
    minus_number = abs(number - palin_number)

    temp = minus_number
    rev = 0
    while minus_number > 0:
        dig = minus_number % 10
        rev = rev * 10 + dig
        minus_number = minus_number // 10

    print(True if temp == rev else False)
main()
