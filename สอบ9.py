"""Diamond C."""
def main():
    """code"""
    sec1 = int(input())
    sec2 = int(input())
    sec3 = int(input())
    sec4 = int(input())
    sec5 = int(input())
    num = (sec1//100 % 10) + (sec2//1000 % 10) + (sec2//10 % 10) + \
          (sec3//10000 % 10) + (sec3 % 10) + (sec4//1000 % 10) + (sec4//10 % 10) +\
          (sec5//100 % 10)
    print(num)
main()
