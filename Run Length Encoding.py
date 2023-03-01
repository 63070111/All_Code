"""Run Length Encoding"""
def main(number):
    """นับว่ามีกี่ตัว"""
    new_string = ""
    current = number[0]
    count = 0
    for i in number:
        if i == current:
            count += 1
        else:
            new_string += str(count) + current
            current = i
            count = 1
    new_string += str(count) + current
    print(new_string)
main(input())
