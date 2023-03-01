"""PhoneNumber"""
def number():
    """เบอร์โทรศัพท์"""
    phone = input()
    country = input()
    if country == "International":
        phone = "+66" + phone[1:]
    print(phone[:-8], phone[-8:-4], phone[-4:])
number()
