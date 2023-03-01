"""[Midterm] Turnstile"""
def walkway():
    """Turnstile"""
    kiosk = "0"
    while True:
        value = input()
        value1 = value.upper()
        if value1 == "END":
            break
        else:
            kiosk += value1
    print(kiosk.count("CP"))
walkway()
