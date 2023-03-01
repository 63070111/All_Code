"""BootSequence"""
def between(number):
    """ใส่เครื่องหมายตรงกลาง"""
    for i in range(1, number):
        if i <= number:
            print(i, "", sep="_", end="")
    print(number)
between(int(input()))


