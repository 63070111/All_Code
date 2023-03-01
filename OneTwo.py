"""OneTwo"""
def number(word):
    """ต่อเลข"""
    if word == 1:
        print('1')
    elif word == 2:
        print('2')
    elif word == 3:
        print('21')
    one = '2'
    two = '21'
    three = ''
    for _ in range(4, word+1):
        three = two + one
        one = two
        two = three
    print(three)
number(int(input()))

