"""[Midterm] SecondConverter"""
def time(total, seconds, minutes, hour):
    """คิดเวลา"""
    second = total % seconds
    scrap = total // seconds
    minute = scrap % minutes
    scrap1 = scrap // minutes
    day = scrap1 % hour
    print(day, minute, second, sep=":")
time(int(input()), int(input()), int(input()), int(input()))
