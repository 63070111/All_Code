"""Standard Normal Distribution"""
def main():
    """5"""
    import math
    num = float(input())
    result = pow(math.e, (-0.5)*pow(num, 2))/math.sqrt(2*math.pi)
    result = '%.5f' %result
    print(result)
main()





