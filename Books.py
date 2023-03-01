"""Books"""
def notebook(book, page, mix1, mix2):
    """อ่านรวม"""
    import math
    total = 0
    for j in range(book):
        if math.ceil(mix1/mix2*page) == page:
            total = total + book - j
            break
        scan = 0
        while scan < page:
            scan = scan + math.ceil(mix1/mix2*page)
            mix1 = mix1 + 1
            mix2 = mix2 + 1
            total = total + 1
    print(total)
notebook(int(input()), int(input()), int(input()), int(input()))
