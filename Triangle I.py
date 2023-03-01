"""Triangle I"""
def triangle(tri1, tri2, tri3, tri4, tri5):
    """สร้าง 3 เหลี่ยม"""
    tri5 = tri5 - 1
    if tri1 > tri2:
        tri4 = tri3
        tri3 = tri2
        tri2 = tri1
    else:
        tri4 = tri3
        tri3 = tri1
    if tri5 > 0:
        triangle(float(input()), tri2, tri3, tri4, tri5)
    else:
        top, middle, low = tri2, tri3, tri4
        result = (middle**2) + (low**2)
        if abs(top**2 - result) <= 0.01:
            print("Yes")
        else:
            print("No")
triangle(float(input()), 0, 0, 0, 3)
