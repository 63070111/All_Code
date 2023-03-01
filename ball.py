"""ball"""
def ball(bounce):
    """ความสูงการเด้งของบอล"""
    hight = bounce
    total = 0
    while hight > 0.01:
        hight = (3/5)*hight
        hight2 = hight
        if hight2 < 0.01:
            break
        total += 1
    print(total)
ball(float(input()))
