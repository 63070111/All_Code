"""PongYa"""
def game(number):
    """นับเลข"""
    if number[-1] == '3':
        print("PONG")
    elif int(number) % 3 == 0:
        print("PONG")

    else:
        print(number)
game(input())
