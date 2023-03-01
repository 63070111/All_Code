"""Airplane"""
def main():
    """v"""
    string = input().upper()
    new_string = ""
    for i in string:
        new_string += i + "-"

    middle_row = "|" + new_string.rstrip("-") + "|"
    print("-" * len(middle_row))
    print(middle_row)
    print("-" * len(middle_row))


main()

