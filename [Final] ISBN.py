"""[Final] ISBN"""
def ball():
    """เดาๆ"""
    text1 = input().replace('-', '')
    word = [int(i) for i in text1[:9]]
    text = ((10*int(word[0]))+(9*int(word[1]))+(8*int(word[2]))+(7*int(word[3]))+(6*int(word[4]))
            +(5*int(word[5]))+(4*int(word[6]))+(3*int(word[7]))+(2*int(word[8])))
    total = -(text)%11
    if str(total) == text1[-1] or (text1[-1] == 'X' and total == 10):
        print("Yes")
    else:
        if total == 10:
            print("No", 'X')
        else:
            print("No", total)
ball()
