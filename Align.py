"""Align"""
def label(size, direction, word):
    """ป้ายบอกทาง"""
    text = size - len(word)
    if direction == "right":
        print(word.rjust(size))
    elif direction == "left":
        print(word.ljust(size))
    elif direction == "center":
        print(" "*(text//2+text % 2) + word + " "*(text//2))
label(int(input()), input(), input())
