""""BrickBridge"""
def build_bridge(bricka, brickb, goal):
    """brick"""
    bridge = goal//5
    left = goal % 5
    if bridge > brickb:
        num = goal - (brickb*5)
        if num > bricka:
            print(-1)
        else:
            print(num)
    else:
        if left == 0:
            print(0)
        else:
            if left > bricka:
                print(-1)
            else:
                print(left)
build_bridge(int(input()), int(input()), int(input()))
