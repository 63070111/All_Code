"""Ping"""
def runprogram(space=0, free=""):
    """รันงาน"""
    first = ''
    one, two, three = 0, 0, 0
    for i in range(7):
        word = input()
        if i == 0:
            first = word[word.find('ping')+5:]
        if i == 2 and '[' and ']' in word:
            first = word[word.find('[')+1:word.find(']')]
        if word.count('time=') != 0:
            free = int(word[word.find('time')+5:word.find('ms')])
            three += free
            if one == 0:
                two = free
            if free > one:
                one = free
            if two > free:
                two = free
        if word.count('Reply from') != 0:
            space += 1
    print('Ping statistics for %s:' %(first))
    print('    Packets: Sent = 4, Received = %d, Lost = %d (%s loss),'
          % (space, (4-space), str((4-space)*25)+'%'))
    if space != 0:
        print('Approximate round trip times in milli-seconds:')
        print('    Minimum = %dms, Maximum = %dms, Average = %dms'
              % (two, one, three/space))
runprogram()
