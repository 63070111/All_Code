"""Timing"""
def main():
    """เย้"""
    number = int(input())
    minute = number // 60
    seconds = number % 60
    hours = minute // 60
    minute = minute % 60
    days = hours // 24
    hours = hours % 24
    print(days, hours, minute, seconds)
main()
