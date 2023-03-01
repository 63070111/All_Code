"""ITKMITL!"""
def main():
    """ดูคำจร้า"""
    string = input().lower()
    if string.count("i") < 2 or string.count("t") < 2 or \
            "k" not in string or "m" not in string or "l" not in string:
        print("No")
    else:
        print("Yes")
main()
