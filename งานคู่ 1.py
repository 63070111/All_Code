"""Sphere"""
def main():
    """เย้"""
    import math
    num = float(input())
    nim = 4*math.pi*((num/2)**2)
    nom = (4/3)*(math.pi*(num/2)**3)
    print("Area :", "%0.3f"%(nim), " square centimeters\n")
    print("Volume :", "%0.3f"%(nom), " cubic centimeters")
main()
