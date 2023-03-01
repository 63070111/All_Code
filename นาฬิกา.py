"""Time Conversion"""
def main():
    """เวลา"""
    seconds = int(input())
    hours = int(seconds / 3600)
    seconds = seconds % 3600
    minutes = int(seconds / 60)
    seconds = seconds % 60
    result = '%d hour(s) %d minute(s) %d second(s)' % (hours, minutes, seconds)
    print(result, end=".")
main()
