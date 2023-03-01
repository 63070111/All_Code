"""Sad lift of tuple"""
def tutle():
    """4 เหลี่ยม"""
    number = input().split(" ")
    nim = input()
    num = number.index(nim)
    nom = number.count(nim)
    for _ in range(nom):
        for _ in range(nom):
            print(num, end=" ")
        print()
tutle()
