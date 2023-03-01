"""Timing II"""
def time(second):
    """Timing II"""
    seconds = second % 60
    minute = second // 60
    minutes = minute % 60
    hours = minute // 60
    hours1 = hours % 24
    days = hours // 24
    day1 = second // 86400
    if day1 <= 9999:
        print("%04d:%02d:%02d:%02d"%(days, hours1, minutes, seconds))
    else:
        print("ERR_:__:__:__")
time(int(input()))


