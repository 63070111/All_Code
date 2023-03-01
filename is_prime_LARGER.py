"""is_prime_LARGER"""
def number(num):
    """รวดเร็ว"""
    if num % 2 == 0 and num != 2:
        print('False')
    elif num > 1:
        for count in range(3, int(num**0.5)+1, 2):
            if num % count == 0:
                print('False')
                break
        else:
            print('True')
    else:
        print('False')
number(int(input()))
