"""FoodGrade I"""
def check_chicken(number, time=1, count=0):
    """food"""
    if number >= 50 and number <= 70:
        count += 1
    if time <= 23:
        return check_chicken(int(input()), time + 1, count)

    return count

print(check_chicken(int(input())))












