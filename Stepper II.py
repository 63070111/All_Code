"""Stepper II"""
def number():
    """Stepper II"""
    num_1 = int(input())
    num_2 = int(input())

    if num_1 < num_2:
        sorting = 1
    else:
        sorting = -1

    for i in range(num_1, num_2 + sorting, sorting):
        print(i)
number()
