"""Circular II"""
def circular():
    """Circular"""
    cir_x = float(input())
    cir_y = float(input())
    cir_r = float(input())
    cir2_x = float(input())
    cir2_y = float(input())
    cir2_r = float(input())
    total = ((cir2_x - cir_x)**2 + (cir2_y-cir_y)**2)**0.5
    total2 = cir_r + cir2_r
    if total2 > total:
        print("Yes")
    else:
        print("No")
circular()
