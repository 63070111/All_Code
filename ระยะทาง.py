"""2D Distance"""
def main():
    """ระยะทาง"""
    dis1 = float(input())
    dis2 = float(input())
    dis3 = float(input())
    dis4 = float(input())
    dis5 = (((dis3-dis1)**2)+((dis4-dis2)**2))
    print("Distance = %.03f" %((dis5)**0.5))
main()


