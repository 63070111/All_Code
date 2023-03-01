"""Multiplication Table"""
def main(n):
    """ตารางสูตรคููณ"""
    print(int(n))
    for i in range(2, 12+1):
        print("%d * %d = %d" %(n, 1, n*i))

for i in range(2, 12 + 1):
    main(i)
    print("---------------")



