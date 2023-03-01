"""Seeker"""
def word(text):
    """หาเลข"""
    wight = " "
    total = 0
    for i in text:
        if i.isnumeric() == True:
            wight += i
        elif wight == ' ':
            continue
        else:
            total += int(wight)
            wight = ' '
    if wight != ' ':
        total += int(wight)
    print(total)
word(input())

