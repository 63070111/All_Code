"""MissingCard I"""
def card():
    """MissingCard I"""
    one = set()
    two = set()
    word1 = ['S', 'H', 'D', 'C']
    word2 = ['A', 'K', 'Q', 'J']
    for i in word1:
        for j in range(2, 11):
            one.add(str(j) + i)
    for i in word1:
        for j in word2:
            one.add(j+i)
    for _ in range(51):
        cards = input()
        two.add(cards)
    miss = one.difference(two)
    for i in miss:
        print(i)
card()

