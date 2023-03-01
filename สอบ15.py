"""emordnilap II"""
def main():
    """Palindrome 2 ชั้น"""
    number = input()
    palin_number = int(number[::-1])
    sum_number = int(number) + palin_number

    temp = sum_number
    rev = 0
    while sum_number > 0:
        dig = sum_number % 10
        rev = rev * 10 + dig
        sum_number = sum_number // 10

    print(True if temp == rev else False)
main()
