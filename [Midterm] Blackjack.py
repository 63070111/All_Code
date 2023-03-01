"""[Midterm] Blackjack"""
def taro():
    """นับคะแนนการ์ด"""
    number = int(input())
    count1 = 0
    count2 = 0
    for _ in range(number):
        card = input()
        if card.isnumeric():
            card1 = int(card)
            count1 += card1
        elif card == "J" or card == "Q" or card == "K":
            count1 += 10
        elif card + "A":
            count2 += 1
    for _ in range(count2):
        if count1 + 11 + (count2-1) <= 21:
            count1 += 11
        else:
            count1 += 1
    print(count1)
taro()
