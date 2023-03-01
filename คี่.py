"""odd / even"""
def main():
    """main"""
    num = int(input())

    if num % 2 != 0:
        print("Weird")
    if 2 < num % 2 == 0 < 5:
        print("Not Weird")
    if 6 < num % 2 == 0 < 20:
        print("Weird")
    if num % 2 == 0 > 20:
        print("Not Weird")
main()


