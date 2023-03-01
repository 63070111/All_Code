"""[Midterm] Lotto"""
def lotto():
    """หาห่วย"""
    number_1st = input()
    number_tail_2 = input()
    number_head_3_1 = input()
    number_head_3_2 = input()
    number_tail_3_1 = input()
    number_tail_3_2 = input()
    number_input = input()

    price = 0
    if number_input == number_1st:
        price += 6000000
    else:
        if number_1st == "000000":
            if number_input == "000001" or number_input == "999999":
                price += 100000
        elif number_1st == "999999":
            if number_input == "000000" or number_input == "999998":
                price += 100000
        else:
            sibling_1 = str(int(number_1st) - 1).zfill(6)
            sibling_2 = str(int(number_1st) + 1).zfill(6)
            if number_input == sibling_1 or number_input == sibling_2:
                price += 100000

    if number_input[4:] == number_tail_2:
        price += 2000

    if number_input[:3] == number_head_3_1:
        price += 4000

    if number_input[:3] == number_head_3_2:
        price += 4000

    if number_input[3:] == number_tail_3_1:
        price += 4000

    if number_input[3:] == number_tail_3_2:
        price += 4000

    print(price)

lotto()
