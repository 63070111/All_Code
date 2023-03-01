"""Circular I"""
def mosquito():
    """cir"""
    me_x = float(input())
    me_y = float(input())
    dian = float(input())
    mos_x = float(input())
    mos_y = float(input())
    distance = ((me_x - mos_x)**2 + (me_y - mos_y)**2)**0.5
    if distance <= dian:
        print("Yes")
    else:
        print("No")
mosquito()
