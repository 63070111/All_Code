"""Day2011"""
def days(day, month):
    """หาวัน"""
    day1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = sum(day1[:month-1]) + day
    total = year % 7
    week = ["Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday"]
    return week[total]
print(days(int(input()), int(input())))
