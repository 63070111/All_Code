"""KuruKuru Turn Around"""
def main():
    """ตำแหน่ง"""
    import math
    xen = float(input())
    yen = float(input())
    degree = int(input())
    radian = -math.radians(degree)
    result_x = xen * math.cos(radian) - yen * math.sin(radian)
    result_y = xen * math.sin(radian) + yen * math.cos(radian)
    result = '%.3f %.3f'% (result_x, result_y)
    print(result)
main()
