"""One For All"""
def people():
    """จำนวนคน"""
    number = int(input())
    name = " ".rstrip()
    for i in range(1, number+1):
        if i == number:
            name = name + input() + "_" + str(number)
        elif i % 2 != 0:
            name = name + input() + "*"*i
        else:
            name = name + input() + "-"*i
    print(name)
people()
