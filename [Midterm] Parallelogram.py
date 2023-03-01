"""[Midterm] Parallelogram"""
def picture():
    """เอียง"""
    text = input()
    lenght = len(text)
    num = 1
    for i in range(lenght, 0, -1):
        print(" "*(i-1), end="")
        for j in text[0:num]:
            print(j, end="")
        num += 1
        print()
    for i in range(1, lenght+1):
        for j in text[i:]:
            print(j, end="")
        print()

picture()
