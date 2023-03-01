"""BTSMRT"""
def bts(name, age, high):
    """ขึ้นรถตามโอกาส"""
    if name == "Children Day" and age < 14.00 and high <= 140.00:
        print("FREE")
    elif name == "Normal Day" and age < 14.00 and high < 90:
        print("FREE")
    elif name == "Senior Day" and 60.00 <= age or age < 14.00 and high < 90:
        print("FREE")
    else:
        print("PAY")
bts(input(), float(input()), float(input()))
