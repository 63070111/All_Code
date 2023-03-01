"""Pringles"""
def candy(pice1, pice2, pice3, hand):
    """ขนม"""
    eaten = pice2.count(')', 0, hand)
    num_pice2 = ' '*hand + pice2[hand:]
    left = num_pice2.count(')')
    print(eaten)
    if left > 0:
        print("There are still some left.")
    else:
        print("None.")
    print(pice1)
    print(num_pice2)
    print(pice3)
candy(input(), input(), input(), int(input()))

