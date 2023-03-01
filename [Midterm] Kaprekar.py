"""[Midterm] Kaprekar"""
def num():
    """หาค่า"""
    number = input()
    count = 0
    while number != "6174":
        ascend = ascending_number(number)
        descend = ascend[::-1]
        number = str(int(descend) - int(ascend)).ljust(4, '0')
        count += 1

    print(count)
def ascending_number(nim):
    """ดูรอบ"""
    n_list = list(map(int, nim))
    for _ in range(len(n_list)):
        for j in range(len(n_list) - 1):
            if n_list[j] > n_list[j + 1]:
                n_list[j + 1], n_list[j] = n_list[j], n_list[j + 1]

    n_list = list(map(str, n_list))
    return "".join(n_list)
num()




