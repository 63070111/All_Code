"""Forbidden Numbers"""
def main():
    """Forbidden Numbers"""
    number_n = int(input())
    number_of_q = int(input())

    q_string = ""
    for i in range(number_of_q):
        q_string += input() + ","

    q_array = q_string.rstrip(",").split(",")
    position = 1
    for i in range(0, number_n):
        if str(i) in q_array:
            continue

        if position < 5:
            print(str(i).zfill(2), end=" ")
        else:
            print(str(i).zfill(2))
            position = 0

        position += 1
main()
