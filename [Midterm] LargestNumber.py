"""[Midterm] LargestNumber"""
def stair(cat1, cat2, cat3):
    """[Midterm]"""
    real1 = str(abs(cat1)) + str(abs(cat2)) + str(abs(cat3))
    real2 = str(abs(cat1)) + str(abs(cat3)) + str(abs(cat2))
    real3 = str(abs(cat2)) + str(abs(cat1)) + str(abs(cat3))
    real4 = str(abs(cat2)) + str(abs(cat3)) + str(abs(cat1))
    real5 = str(abs(cat3)) + str(abs(cat1)) + str(abs(cat2))
    real6 = str(abs(cat3)) + str(abs(cat2)) + str(abs(cat1))
    if int(real1) >= int(real2) and int(real1) >= int(real3) and int(real1) >= int(real4) and \
            int(real1) >= int(real5) and int(real1) >= int(real6):
        print(int(real1))
    elif int(real2) >= int(real1) and int(real2) >= int(real3) and int(real2) >= int(real4) and \
            int(real2) >= int(real5) and int(real2) >= int(real6):
        print(int(real2))
    elif int(real3) >= int(real1) and int(real3) >= int(real2) and int(real3) >= int(real4) and \
            int(real3) >= int(real5) and int(real3) >= int(real6):
        print(int(real3))
    elif int(real4) >= int(real1) and int(real4) >= int(real2) and int(real4) >= int(real3) and \
            int(real4) >= int(real5) and int(real4) >= int(real6):
        print(int(real4))
    elif int(real5) >= int(real1) and int(real5) >= int(real2) and int(real5) >= int(real3) and \
            int(real5) >= int(real4) and int(real5) >= int(real6):
        print(int(real5))
    else:
        print(int(real6))
stair((int(input())), (int(input())), (int(input())))
