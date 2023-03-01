"""[Midterm] Stair"""
def cat():
    """ขั้นบันได"""
    leg = int(input())
    step = 0
    valid = 0
    break_point = False

    stairs = int(input())
    for _ in range(stairs):
        stair = int(input())

        if stair > leg:
            print("NO")
            break_point = True
            break
        else:
            if valid + stair <= leg:
                valid += stair
            else:
                step += 1
                valid = stair
    else:
        step += 1
    if not break_point:
        print(step)
cat()
