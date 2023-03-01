"""[Midterm] FourDirecitons"""
def give_up(line_number):
    """ขึ้น"""
    if line_number == 1:
        return "  *  "
    if line_number == 2:
        return " *** "
    if line_number == 3:
        return "* * *"
    if line_number == 4:
        return "  *  "
    if line_number == 5:
        return "  *  "

def give_down(line_number):
    """ลง"""
    if line_number == 1:
        return "  *  "
    if line_number == 2:
        return "  *  "
    if line_number == 3:
        return "* * *"
    if line_number == 4:
        return " *** "
    if line_number == 5:
        return "  *  "

def give_right(line_number):
    """ขวา"""
    if line_number == 1:
        return "  *  "
    if line_number == 2:
        return "   * "
    if line_number == 3:
        return "*****"
    if line_number == 4:
        return "   * "
    if line_number == 5:
        return "  *  "

def give_left(line_number):
    """ขวา"""
    if line_number == 1:
        return "  *  "
    if line_number == 2:
        return " *   "
    if line_number == 3:
        return "*****"
    if line_number == 4:
        return " *   "
    if line_number == 5:
        return "  *  "

def picture():
    """รูป"""
    pic = input()
    for number in range(1, 6):
        for num in pic:
            if num == "U":
                print(give_up(number), end=" ")
            elif num == "D":
                print(give_down(number), end=" ")
            elif num == "L":
                print(give_left(number), end=" ")
            elif num == "R":
                print(give_right(number), end=" ")
        print()
picture()

