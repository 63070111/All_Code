"""WeightStation"""
def station(average, point1, point2, point3):
    """WeightStation"""
    point4 = average*4-(point1 + point2 + point3)
    if average*4 > 15000:
        print("Overweight")
    elif point1 < average/2 or point1 > average + average/2:
        print("Unbalance")
    elif point2 < average/2 or point1 > average + average/2:
        print("Unbalance")
    elif point3 < average/2 or point1 > average + average/2:
        print("Unbalance")
    elif point4 < average/2 or point1 > average + average/2:
        print("Unbalance")
    else:
        print("Pass", "%.2f"%(point4))
station(float(input()), float(input()), float(input()), float(input()))

