"""Modular Spy"""
def main():
    """เวลา"""
    num = round(float(input()))
    minutes = pow((num + pow(num, 5)), 9876543, 60)
    result = '15:' + str(minutes).zfill(2)
    print(result)
main()
