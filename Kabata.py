"""Kabata"""
def word():
    """เช็คคำ"""
    count = int(input())
    nix = []
    for _ in range(count):
        text = input()
        if text.find('baka') != -1:
            nix.append('no')
            continue
        text = text.replace('bakka', '')
        text = text.replace('ka', '')
        text = text.replace('ba', '')
        text = text.replace('ta', '')
        if text != '':
            nix.append('no')
        else:
            nix.append('yes')
    for i in nix:
        print(i)
word()
