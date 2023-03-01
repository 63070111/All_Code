"""Math Reporter!?"""
def main():
    """เย้"""
    num_1 = int(input())
    num_2 = int(input())
    num_3 = int(input())
    num_4 = int(input())
    num_5 = int(input())
    num_6 = int(input())
    num_7 = int(input())
    num_8 = int(input())
    num_9 = int(input())
    num_10 = int(input())
    min_num = max_num = num_1
    min_num = min(min_num, num_2)
    max_num = max(max_num, num_2)
    min_num = min(min_num, num_3)
    max_num = max(max_num, num_3)
    min_num = min(min_num, num_4)
    max_num = max(max_num, num_4)
    min_num = min(min_num, num_5)
    max_num = max(max_num, num_5)
    min_num = min(min_num, num_6)
    max_num = max(max_num, num_6)
    min_num = min(min_num, num_7)
    max_num = max(max_num, num_7)
    min_num = min(min_num, num_8)
    max_num = max(max_num, num_8)
    min_num = min(min_num, num_9)
    max_num = max(max_num, num_9)
    min_num = min(min_num, num_10)
    max_num = max(max_num, num_10)
    sum_num = num_1 + num_2 + num_3 + num_4 + num_5 + num_6 + num_7 + num_8 + num_9 + num_10
    multiply_num = num_1 * num_2 * num_3 * num_4 * num_5 * num_6 * num_7 * num_8 * num_9 * num_10
    print('max:', max_num)
    print('min:', min_num)
    print('sum:', sum_num)
    print('digit:', len(str(multiply_num)))
main()




