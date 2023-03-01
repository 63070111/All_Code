"""สุตรคูณ"""
def main():
    """เอาเลขสองตัวมาคูณได้แม่ไหนรันแม่นั้น"""
    num = int(input())
    nim = int(input())
    for i in range(1, 10001):
        if i % num == 0:
            if i % nim == 0:
                print(i)
main()

