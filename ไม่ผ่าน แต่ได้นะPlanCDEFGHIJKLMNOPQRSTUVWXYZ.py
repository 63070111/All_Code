"""PlanCDEFGHIJKLMNOPQRSTUVWXYZ"""
def word():
    """plan"""

    order_option = input()
    answer = []
    num_1 = float(input())
    answer.append(num_1)
    num_2 = float(input())

    def compare(order_option, num_1, num_2):
        return num_1 < num_2 if order_option == 'Ascend' else num_1 > num_2

    if compare(order_option, num_1, num_2):
        answer.append(num_2)
    else:
        answer = [num_2] + answer

    num_3 = float(input())
    if compare(order_option, num_3, answer[1]):
        if compare(order_option, num_3, answer[0]):
            answer = [num_3] + answer
        else:
            answer.append(answer[1])
            answer[1] = num_3
    else:
        answer.append(num_3)

    answer[0] = "%.2f" % answer[0]
    answer[1] = "%.2f" % answer[1]
    answer[2] = "%.2f" % answer[2]
    print(", ".join(answer))
