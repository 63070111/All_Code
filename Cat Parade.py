"""Cat Parade"""
def cat():
    """find cats"""
    nix = []
    while True:
        word = input()
        nix += word.split(", ")
        if word == "END":
            nix.remove(word)
            break
        if word == "IT'S A DOG":
            nix.remove(nix[-1])
            nix.remove(nix[-1])
    nix2 = nix.copy()
    for i in list(sorted(set(nix2))):
        print(i, nix2.index(i) + 1, nix2.count(i))
cat()
