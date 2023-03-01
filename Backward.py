"""Backward"""
def back():
    """ย้อน"""
    area = []
    while True:
        data = input()
        if data == "NULL":
            break
        area.append(data)
    area.reverse()
    for i in area:
        print(i)
back()
