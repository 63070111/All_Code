"""Muddled Menu"""


def manu():
    """เมนู"""
    nix = []
    while True:
        word = input()
        if word == 'DONE':
            break
        if word[-1] == 'N':
            nix.extend(word.split(' #N'))
            nix.remove('')
        elif word[-1].isdecimal() == True:
            name = word.split(' #')
            nix.insert(int(name[-1]) - 1, name[0])
        elif word == "SOMETHING'S WRONG":
            nix.clear()
        elif word == 'CLOSED':
            nix.clear()
            break
        else:
            doit = word.split(': ')
            doit.pop(0)
            delete = doit[0]
            deleteword = int(nix.index(delete))
            del nix[deleteword]
    total = []
    total.extend(nix)
    total.reverse()
    print('Full Course: %s Reversed: %s' % (nix, total))


manu()
