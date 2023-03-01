"""Runner"""
def word(run):
    """Runner"""
    win = -1, -1, -1
    for _ in range(int(input())):
        data = input().split()
        begin = int(data[1])
        speed = int(data[0])
        time = (run - begin) / speed
        if win[0] > time or (win[0] == time and speed > win[1]) or win[0] == -1:
            win = time, speed, _+1
    print(win[2])
word(int(input()))
