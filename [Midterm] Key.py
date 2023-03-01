"""[Midterm] Key"""
def key():
    """[Midterm] Key"""
    word = input()
    total = int(word[0]) + int(word[1]) + int(word[2]) + \
            int(word[3]) + int(word[4]) + int(word[5]) + \
            int(word[6]) + int(word[7]) + int(word[8]) + \
            int(word[9]) + int(word[10]) + int(word[11]) + int(word[12])
    last = int((word[10] + word[11] + word[12]))*10
    full = str(total + last)
    if int(full) > 1000:
        print(full[-4::])
    elif int(full) < 1000:
        num = int(full)+1000
        print(num)
key()
