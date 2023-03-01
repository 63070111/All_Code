"""[Final 2019] ไพ่"""
def book(text):
    """สับไพ่"""
    while True:
        number = input()
        if number == "END":
            break
        text.append(number)
    text = [int(i) for i in text]
    for nit in range(1, len(text)):
        nat = nit - 1
        while text[nat] > text[nit] and nat >= 0:
            nat = nat - 1
        text.insert(nat+1, text[nit])
        text.pop(nit+1)
    text = [str(i) for i in text]
    return text
def sat():
    """ไพ่"""
    string = '\n'.join(book([]))
    print(string)
sat()
