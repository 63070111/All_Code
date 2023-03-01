"""Secret Code"""
def main():
    """รหัสลับ"""
    sec1 = int(input())
    sec2 = int(input())
    sec3 = int(input())
    sec4 = int(input())
    sec5 = int(input())
    num = (sec1%10)+(sec2//10%10)+(sec3//100%10)+\
          (sec4//1000%10)+(sec5//10000%10)
    print((sec1 % 10), (sec2//10 % 10), (sec3//100 % 10),
          (sec4//1000 % 10), (sec5//10000 % 10), sep="+", end=" = ")
    print(num)
main()






