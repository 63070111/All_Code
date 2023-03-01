"""Day I"""
def month(year):
    """Day I"""
    if year % 4 == 0 and year % 100 != 0:
        print("Yes")
    elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        print("Yes")
    else:
        print("No")
month(int(input()))
