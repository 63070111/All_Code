"""[Midterm] Sequence N"""
def picture(num):
    """N"""
    for num_x in range(num):
        for num_y in range(num):
            if num_y == 0 or num_y == num-1 or num_x == num_y:
                print("*", end="")
            else:
                print(" ", end="")
        print()
picture(int(input()))
