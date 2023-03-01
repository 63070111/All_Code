"""While loop appeared!"""
def main():
    """pokemon"""
    catch = 0
    previous_action = ""
    while True:
        action = input()
        if action == "END":
            break
        elif action == "Wild pokemon appeared!" and previous_action == "grass":
            catch += 1

        previous_action = action

    if catch > 0:
        print("Captured %d pokemon!" % catch)
    else:
        print("Maybe later")
main()
