"""[Midterm] Bill"""
def bill():
    """ราคาที่ต้องจ่าย"""
    money = float(input())
    total = (money*0.01)*50
    full = money + total
    full1 = full + full*0.07
    print("%.2f"%full1)
bill()

