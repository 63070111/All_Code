"""cat expo T^T"""
def main():
    """cat"""
    from datetime import datetime
    day = int(input())
    month = int(input())
    hour = int(input())
    minute = int(input())
    date = datetime(2020, month, day, hour, minute)
    if date >= datetime(2020, 6, 22, 10, 0) and date < datetime(2020, 6, 22, 14, 0):
        print("P'Namo is waiting for event.")
        print("ticket 1000 Baht.")
        print("Rare CD!!")
    elif date >= datetime(2020, 7, 11, 10, 0) and date < datetime(2020, 7, 11, 14, 0):
        print("P'Namo is waiting for event.")
        print("ticket 1300 Baht.")
        print("Rare CD!!")
    elif date >= datetime(2020, 7, 11, 14, 0) and date < datetime(2020, 11, 21, 0, 0):
        print("P'Namo is waiting for event.")
        print("ticket 1500 Baht.")
    else:
        print("See you Cat expo 7.")
main()



