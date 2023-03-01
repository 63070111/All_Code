"""Hexagonal Prism"""
def main():
    """วาดรูป"""
    import math
    base_edge = float(input())
    height = float(input())
    surface_area_cm = (6 * base_edge * height) + \
                      (3 * math.sqrt(3) * math.pow(base_edge, 2))
    surface_area_m = '%.2f' % (surface_area_cm / 10000)
    print(surface_area_m, end=" squaremetre ")
main()


