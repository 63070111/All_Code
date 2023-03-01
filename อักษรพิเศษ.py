"""[Midterm] ValidVar"""
def main():
    """ValidVar"""
    name = '!"#$%&\'()*+,-./:;<=>?@[\\]^`{|}~'
    word = "if else elif while for True False continue break " \
           "return is in and or from as pass not def None"
    total = int(input())
    for _ in range(total):
        varible = input().strip()
        still_legit = True

        for pun in name:
            if pun in varible:
                print("Invalid")
                still_legit = False
                break

        if still_legit:
            if " " in varible:
                print("Invalid")
                still_legit = False
        if still_legit:
            if varible[0].isdigit():
                print("Invalid")
                still_legit = False
        if still_legit:
            if " " + varible + " " in word:
                print("Invalid")
                still_legit = False

        if still_legit:
            print("Valid")
main()