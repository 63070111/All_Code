"""centerrrrrrr"""
def main():
    """โอว้"""
    number = int(input())
    string = input()
    middle_count = int((number - len(string)) / 2)
    print('=' * number)
    print('-' * middle_count + string + '-' * middle_count)
    print('=' * number)
main()

