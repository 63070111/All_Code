"""isPrime_large"""
def prime(number):
    """เฉพาะ"""
    import math
    if number < 2:
        print("False")
        return
    for i in range(2, int(math.log(number, 2)) + 1):
        if number % i == 0:
            print("False")
            return
    print("True")
prime(int(input()))
