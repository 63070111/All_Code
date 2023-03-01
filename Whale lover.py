"""Whale lover"""
def main():
    """Whale lover"""
    found = int(input())
    water_pokemon = 0
    found_whale = False
    for _ in range(found):
        location = input()
        name = input()
        category = input()
        if name == "wailmer" or name == "wailord":
            found_whale = True
            break

        if category == "water" and location == "water":
            water_pokemon += 1

    if found_whale:
        print("WHALE IS THE BEST!")
    else:
        if water_pokemon > 0:
            print("Found %d water pokemon." % water_pokemon)
        else:
            print("Bad omen againnn.")
main()
