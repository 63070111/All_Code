"""[Recommend][Final] BloodDonation"""
def upset():
    """ตรวจ"""
    age = int(input())
    weight = int(input())
    count = int(input())
    book = input()
    one = [17 < age <= 70 and weight >= 45]
    two = [age == 17 and weight >= 45]
    #three = [count == 0 and age <= 55]
    four = [60 <= age <= 70 and book == 'True' and weight >= 45]

    if one:
        if four:
        print('Yes')
    elif two and book == 'True':
        print('Yes')


    else:
        print('No')
upset()
