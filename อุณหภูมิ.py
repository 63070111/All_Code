"""GoH ที่ไม่ใช่ในการ์ตูน! (2)"""
def main():
    """ร้อน"""
    cel = int(input())
    rankine = (cel + 273.15) * (9 / 5)
    kelvin = cel + 273.15
    fahrenheit = cel * (9 / 5) + 32
    newton = cel * 0.33
    delisle = (100 - cel) * 1.5
    a_temp = rankine - kelvin + fahrenheit - (newton / delisle)
    result = '%.2f A' % a_temp
    print(result)
main()
