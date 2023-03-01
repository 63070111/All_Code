"""RockPaperScissor"""
def win():
    """แข่งงง"""
    couple = input()
    scorea = 0
    scoreb = 0
    speace = len(couple)
    one = 0
    two = 1
    while speace != 0:
        if couple[one] == "R" and couple[two] == "S":
            scorea += 1
        elif couple[one] == "P" and couple[two] == "R":
            scorea += 1
        elif couple[one] == "S" and couple[two] == "P":
            scorea += 1
        elif couple[one] == couple[two]:
            pass
        else:
            scoreb += 1
        one += 2
        two += 2
        speace -= 2
    if scorea > scoreb:
        print('A win ' + str(scorea) + '-' + str(scoreb))
    elif scorea < scoreb:
        print('B win ' + str(scoreb) + '-' + str(scorea))
    else:
        print('DRAW ' + str(scorea))
win()
