"""4"""
def main():
    """เช็คว่ามีเลขหรือลำดับเท่ากับ4"""
    string = input()
    sub_string = input()
    result = string.count(sub_string)
    result1 = string.count("4")
    if result == 4 or result1:
        print("It's not as safe as you think, Mista...")
    else:
        print("MISTA, THIS ONE'S 4 U")
main()


