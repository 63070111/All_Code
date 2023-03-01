"""SurprisingVote"""
def gift(totol, rise):
    """Vote"""
    diff = totol-rise
    same = (diff*(diff <= rise) + rise*(rise < diff))
    less = diff - same
    if rise - less > 2:
        print("Surprising")
    else:
        print("Not surprising")
gift(float(input()), float(input()))


