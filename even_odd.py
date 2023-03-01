"""even_odd"""
def main():
    """even_odd"""
    number = int(input())
    number_type = input()
    condition = 0 if number_type == "Even" else 1
    for i in range(number):
        j = i + 1
        if j % 2 == condition:
            print("Found %s Yay!" % number_type)
        else:
            print(j)
main()
