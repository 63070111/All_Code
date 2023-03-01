"""Multiplication Table"""
def main():
    """Multiplication Table"""
    number = int(input())
    for i in range(2, number+1):
        print("---------------")
        for j in range(1, 13):
            print("%d x %d\t = %d" % (i, j, i * j))
        print("---------------")
main()
