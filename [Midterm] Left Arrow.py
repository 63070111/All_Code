"""[Midterm] Left Arrow"""
def arrow(num, tall):
    """[Midterm]"""
    for i in range(tall//2, 0, -1):
        print(i * " " + "*" * num)
    print("*"*num)
    for j in range(1, tall//2+1):
        print(j * " " + "*" * num)
arrow(int(input()), int(input()))
