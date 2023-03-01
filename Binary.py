"""Binary"""
def two(number):
    """เลขฐาน2"""
    bun = []
    dec = number
    if number == 0:
        print("0")
    while dec > 0:
        bun.append(str(dec % 2))
        dec = int(dec / 2)
    bun.reverse()
    print(''.join(bun))
two(int(input()))
