"""Run Length Decoding"""
def number():
    """เพิ่มตามเลข"""
    value = input()
    space = " "
    for i in value:
        if i.isdecimal() == True:
            space = space + i
        else:
            space = int(space)
            print(i*space, end="")
            space = str(0)
number()
