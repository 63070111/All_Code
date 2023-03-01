"""[Final] WPM"""
def finger(one, two):
    """นับ"""
    if one == "Kids":
        if two < 11:
            print("Very Slow")
        elif 11 <= two <= 20:
            print("Slow")
        elif 21 <= two <= 30:
            print("Average")
        elif 31 <= two <= 40:
            print("Fast")
        else:
            print("Very Fast")

    else:
        if two < 26:
            print("Very Slow")
        elif 26 <= two <= 35:
            print("Slow/Beginner")
        elif 36 <= two <= 45:
            print("Intermediate/Average")
        elif 46 <= two <= 65:
            print("Fast/Advanced")
        elif 66 <= two <= 80:
            print("Very Fast")
        else:
            print("Insane")
finger(input(), int(input()))
