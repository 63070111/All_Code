from datetime import datetime
    day = int(input())
    month = int(input())
    hour = int(input())
    minute = int(input())
    date = datetime(2020, month, day, hour, minute)
    if date >= datetime(2020, 6, 22, 10, 0) and date < datetime(2020, 6, 22, 14, 0):
        print("P'Namo is waiting for event.\n"
              "ticket 1000 Baht.\nRare CD!!")
    elif date >=datetime(2020, 7, 11, 10, 0) and date < datetime(2020, 7, 11, 14, 0):
        print("P'Namo is waiting for event.\n"
              "ticket 1300 Baht.\nRare CD!!")
    elif date >= datetime(2020, 7, 11, 14, 0) and date < datetime(2020, 11, 20, 0, 0):
        print("P'Namo is waiting for event."
              "\nticket 1500 Baht.")
    else:
        print("See you Cat expo 7.")