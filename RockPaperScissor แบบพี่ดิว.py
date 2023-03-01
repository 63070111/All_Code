"""RockPaperScissor"""

def rps(vluea, vlueb):
    """เปายิ้งฉุบ"""
    rule = {'R': {'R': (0, 0), 'P': (0, 1), 'S': (1, 0)},
            'P': {'R': (1, 0), 'P': (0, 0), 'S': (0, 1)},
            'S': {'R': (0, 1), 'P': (1, 0), 'S': (0, 0)}}
    return rule[vluea][vlueb]

scorea = 0
scoreb = 0
text = input()
for i, sign in enumerate(text):
    if i % 2 == 0:
        score = rps(text[i], text[i + 1])
        scorea += score[0]
        scoreb += score[1]
if scorea > scoreb:
    print('A win ' + str(scorea) + '-' + str(scoreb))
elif scorea < scoreb:
    print('B win ' + str(scoreb) + '-' + str(scorea))
else:
    print('DRAW ' + str(scorea))
