"""This is My House"""
def main():
    """This is My House"""
    name = input()
    print("", "%s" % ("_"*(len(name)-2)), "")
    print("/%s\\" % ("_" * (len(name)-2)))
    print("|%s%s%s|" % (" "*((len(name) - 4) // 2), "_" * 3, " " * ((len(name) - 4) // 2)))
    print("|%s|%s|%s|" % (" "*((len(name)-7) // 2), " " * 3, " " * ((len(name) - 7) // 2)))
    print("|%s|%so|%s|" % (" "*((len(name)-6) // 2), " " * 2, " " * ((len(name) - 6) // 2)))
    print("|%s|%s|%s|" % ("_"*((len(name)-6) // 2), "_" * 3, "_" * ((len(name) - 6) // 2)))
    print("%s" % name)
main()




