"""Converting"""
def main():
    """ค่าหลัก"""
    number = int(input())
    orig_number = number
    magnitude = 0
    while abs(number) >= 1000:
        magnitude += 1
        number /= 1000.0

    if orig_number % 1000 in [0, orig_number]:
        print('%d%s' % (number, ['', 'K', 'M', 'B'][magnitude]))
    else:
        print('%.1f%s' % (number, ['', 'K', 'M', 'B'][magnitude]))
main()
