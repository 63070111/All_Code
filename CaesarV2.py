"""CaesarV2"""
def main():
    """V2"""
    massage = input()
    case = []
    for word in range(27):
        text = []
        for i in massage:
            conven = ord(i)
            if conven >= 97 and conven <= 122:
                conven += word
                while conven > 122:
                    conven -= 26
                while conven < 97:
                    conven += 26
            elif conven >= 65 and conven <= 90:
                conven += word
                while conven > 90:
                    conven -= 26
                while conven < 65:
                    conven += 26
            new = chr(conven)
            text.append(new)
        case.append(text)
    loss = []
    for i in case:
        check = ''
        for j in i:
            check += j
        loss.append(check)
    for i in loss:
        if 'the' in i:
            total = i
    print(total)
main()

