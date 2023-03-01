"""[Midterm] ValidVar"""
def check_name():
    """check"""
    number = int(input())
    total = ""
    value = ['if', 'else', 'elif', 'while', 'for', 'True', 'False', 'continue', 'break',
             'return', 'is', 'in', 'and', 'or', 'from', 'as', 'pass', 'not', 'def', 'None']
    for _ in range(number):
        space = input()
        space = space.lstrip(" ")
        space = space.rstrip(" ")
        check_number = space[0]
        if check_number.isnumeric() == True:
            tal = "Invalid"
        elif space.find(" ") >= 1:
            tal = "Invalid"
        elif space.isidentifier() == False:
            tal = "Invalid"
        elif space in value:
            tal = "Invalid"
        else:
            tal = "Valid"
        total = total + tal + "\n"
    print(total.rstrip("\n"))
check_name()
