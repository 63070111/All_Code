"""[Midterm] Harshad"""
def nummber():
    """Harshad"""
    for _ in range(10):
        num = 0
        digit = int(input())
        count = str(abs(digit))
        if digit == 0:
            print("No")
            continue
        for j in count:
            num += int(j)
        check = digit % num
        if check == 0:
            print("Yes")
        else:
            print("No")
nummber()
