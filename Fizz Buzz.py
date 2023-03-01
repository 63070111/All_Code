"""Fizz Buzz"""
def word(number):
    """Fizz Buzz"""
    for i in range(1, number+1):
        j = i
        if j % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif j % 3 == 0:
            print("Fizz")
        elif j % 5 == 0:
            print("Buzz")
        else:
            print(j)
word(int(input()))

