"""GoH ที่ไม่ใช่ในการ์ตูน! (1)"""
import math
def hun(xun):
    """เย้"""
    return 3 * (xun + 4) - xun * (5 - 3 * xun)


def fun(xun):
    """เย้"""
    return 3 * pow(2, xun) + 2 * pow(xun, 2) * \
           (math.degrees(math.asin(0.5)) + xun)


def gun(xun):
    """เย้"""
    return 4 * pow(xun + 2, 2) + 5 * \
           (xun - 1) + hun(xun - 1)

def main():
    """เย้"""
    xun = int(input())
    result = gun(fun(xun - 2) / hun(xun + 1)) - xun
    result = '%.2f'% result
    print("Answer:", result)
main()









