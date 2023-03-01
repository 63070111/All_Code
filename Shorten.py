"""Shorten"""
def shirt():
    """เสื้อ"""
    begin = 'origin'
    between = None
    while True:
        number = int(input())
        if begin == 'origin' and number == -1:
            break
        elif begin == 'wait' and number == -1:
            print('-', between, sep='', end='')
            break
        elif begin == 'origin' and between == None:
            print(number, end='')
        elif begin == 'origin' and number-between == 1:
            begin = 'wait'
        elif begin == 'origin' and number - between != 1:
            print(',', number, end='')
        elif begin == 'wait' and number - between != 1:
            print('-' + str(between) + ',', number, end='')
            begin = 'origin'
        between = number
shirt()
