"""Prime Number"""
def main():
    """Prime Number"""
    num = 2
    number = int(input())
    pri = ""
    if number < num:
        pri = "No"
    elif number == num:
        pri = "Yes"
    else:
        while num < number:
            if number % num == 0:
                pri = "No"
                break
            else:
                pri = "Yes"
            num = num + 1
    print(pri)
main()


