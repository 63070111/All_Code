"""AlmostMean"""
def main():
    """รันค่า"""
    one = int(input())
    baby = {}
    score = []
    for _ in range(one):
        nom = input().split('\t')
        baby.update({nom[-1]: nom[0]})
        score.append(float(nom[-1]))
    score.sort()
    total = 0
    for i in score:
        two = float(i)
        total += two
    avg = total//len(score)
    nix = []
    for j in score:
        if j > avg:
            pass
        else:
            nix.append(j)
    nix.sort()
    print(baby.get(str(nix[-1]).strip()), str(nix[-1]).strip(), sep='\t')
main()
