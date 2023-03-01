"""Welcome 7echnaldooooo!"""
def main():
    """7echnaldooooo!"""
    weight = float(input())
    hight = (int(input())/100)
    num = hight**2
    nom = round(weight / num)
    if nom >= 30:
        print("you're too fat, lose weight now!")
        return()
    elif 25 <= nom < 30:
        print("you're almost fat, prepare the "
              "losing weight course!")
        return ()
    elif 18.6 <= nom < 25:
        print("pass, welcome Technaldooooo!")
        return ()
    elif num < 18.6:
        print("you're so weak, eat more!")
main()
