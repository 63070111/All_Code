"""Rectangle"""
def square_area():
    """Square area"""
    wide = int(input())
    lenght = int(input())
    print(wide * lenght)
    square_circumference(wide, lenght)

def square_circumference(wide, lenght):
    """Square_circumference"""
    print(2 * (wide + lenght))
square_area()
