"""All_Primes"""
def number(ber):
    """เอาเลขเฉพาะ"""
    nix = 0
    for i in range(1, ber + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                nix += 1
    print(nix)
number(int(input()))
