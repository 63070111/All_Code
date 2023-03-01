"""Middle Sword!"""
def main():
    """sword"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())

    highest = num_1 ^ ((num_1 ^ num_2) & -(num_1 < num_2))
    highest = highest ^ ((highest ^ num_3) & -(highest < num_3))

    lowest = num_1 ^ ((num_2 ^ num_1) & -(num_2 < num_1))
    lowest = lowest ^ ((num_3 ^ lowest) & -(num_3 < lowest))

    result = (num_1 + num_2 + num_3) - highest - lowest
    print(result)
main()
