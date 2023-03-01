"""[Final 2019] Hamming"""
def mean():
    """เทียบค่า"""
    one = (input())
    two = (input())
    total = 0
    for i in range(len(one)):
        if one[i] != two[i]:
            total += 1
    print(total)
mean()
