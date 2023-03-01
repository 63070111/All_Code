"""text box"""
def main():
    """เย้"""
    num = input()
    if len(num) == 0:
        print("", "%s" % ("_"*(len(num) + 2)), "")
        print("|" + " " * (len(num) + 2) + "|" + "\n", end="")
        print("", "%s" % ("_"*(len(num) + 2)), "")
    else:
        print("", "%s" % ("_"*(len(num) + 2)), "")
        print(("|" + " " * (len(num) + 2) + "|" + "\n") * ((len(num)) // 2), end="")
        print(("|" + " " + num + " " + "|"))
        print(("|" + " " * (len(num) + 2) + "|" + "\n") * ((len(num)) // 2), end="")
        print("", "%s" % ("_"*(len(num) + 2)), "")
main()
