"""Robot Barista"""
def main():
    """robot"""
    rob = str(input())
    roba = len(rob)
    roby = int(input())
    yum = max(roba,roby)
    yum2 = min(roba,roby)
    mun = str(yum)+str(yum2**2)
    muny = hex(int(mun))
    print(rob+muny)
main()



