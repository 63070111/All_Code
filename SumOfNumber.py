"""SumOfNumber"""
def number():
    """Sum"""
    line = int(input())
    need = 0
    while need != line:
        total = int(input())
        if total == -1:
            break
        need += total
    print(need)
number()
