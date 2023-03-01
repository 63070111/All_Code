"""The Pyramid"""
def main():
    """The Pyramid"""
    ber = int(input())
    nim = 1
    nom = ber - 1
    for _ in range(0, ber):
        print(" " * nom + "*" * nim)
        nom -= 1
        nim += 2
main()
