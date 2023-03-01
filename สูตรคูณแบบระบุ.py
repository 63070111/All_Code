"""Multiplication Table"""
def main():
    """สูตรคูณตามใจฉัน"""
    num = int(input())
    while(num <= 12):
        jun = 1
        print("---------------")
        while(jun <= 12):
            print("{0} * {1} = {2}".format(num, jun, num*jun))
            jun = jun + 1
        num = num+1
main()
