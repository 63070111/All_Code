"""FOR!F-Ball"""
def ballcup():
    """หาลูกบอล"""
    position = [1, 0, 0]
    ball = input()
    count = 0
    for check in ball:
        number = 0
        if check == 'A' or check == 'a':
            number = position[0]
            position[0] = position[1]
            position[1] = number
        elif check == 'B' or check == 'b':
            number = position[1]
            position[1] = position[2]
            position[2] = number
        else:
            number = position[0]
            position[0] = position[2]
            position[2] = number
    while count < 3:
        if position[count] == 1:
            print(count + 1)
        count += 1
ballcup()
