"""Binary to ten"""
def number(two):
    """ฐาน2"""
    value = 0
    count = len(two)
    for i in two:
        count = count - 1
        if int(i) != 0:
            value = value*2**count
    print(value)
number(str(input()))
