"""9"""
def main():
    """9"""
    string = input()
    sub_string = "9"
    result = string.count(sub_string)
    result1 = string.count("9")
    nom = 9 - result
    if result >= 9 and result1:
        print("Hooray! This life must go on.")
    elif result < 9 and result1:
        print("My fortune is running out.")
        print("I want", "%d"%(nom), "more!")
    else:
        print("Are you kidding me?!")
main()

