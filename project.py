"""Number Guessing Game"""
import random
attempts_list = []
def show_score():
    if len(attempts_list) <= 0:
        print("There is currently no high score, so sad...")
    else:
        print("The current high score is {} attempts.".format(min(attempts_list)))

def start_game():
    random_number = random.randint(1, 26)
    big_alphabet = {'1':'A', '2':'B', '3':'C', '4':'D', '5':'E', '6':'F', '7':'G', '8':'H', '9':'I', '10':'J',\
                    '11':'K', '12':'L', '13':'M', '14':'N', '15':'O', '16':'P', '17':'Q', '18':'R', '19':'S',\
                    '20':'T', '21':'U', '22':'V', '23':'W', '24':'X', '25':'Y', '26':'Z'}
    small_alphabet = {'1':'a', '2':'b', '3':'c', '4':'d', '5':'e', '6':'f', '7':'g', '8':'h', '9':'i', '10':'j',\
                      '11':'k', '12':'l', '13':'m', '14':'n', '15':'o', '16':'p', '17':'q', '18':'r', '19':'s',\
                      '20':'t', '21':'u', '22':'v', '23':'w', '24':'x', '25':'y', '26':'z'}
    print("Hello traveler! Welcome to the game of guesses!")
    player_name = input("What is your name? \n-> ").capitalize()
    wanna_play = input("Hi, {}. Would you like to play the guessing game? (Enter Yes/No)\n-> ".format(player_name))
    attempts = 0
    while wanna_play.lower() != "yes" and wanna_play.lower() != "no":
        wanna_play = input("That is not the desired answer. (Enter Yes/No)\n-> ")
    while wanna_play.lower() == "yes":
        try:
            your_guess = input("Pick a number between 1 and 26 \n-> ")
            if int(your_guess) < 1 or int(your_guess) > 26:
                raise ValueError("Please guess a number within the given range.")
            if int(your_guess) == random_number:
                print("Nice! You got it!")
                attempts += 1
                attempts_list.append(attempts)
                print("It took you {} attempts".format(attempts))
                if attempts > 26:
                    attempts = attempts%26
                print("Code for you is", big_alphabet[str(random_number)] + \
                      small_alphabet[str(attempts)] + str(random.randint(0, 100)) + \
                      small_alphabet[str(random.randint(1, 26))] + big_alphabet[str(random.randint(1, 26))] + \
                      big_alphabet[str(int(your_guess))] + small_alphabet[str(random.randint(1, 26))] + \
                      str(random_number) + str(random.randint(0, 100)))
                play_again = input("Would you like to play again? (Enter Yes/No) \n-> ")
                attempts = 0
                random_number = int(random.randint(1, 26))
                while play_again.lower() != "yes" and play_again.lower() != "no":
                    play_again = input("That is not the desired answer. (Enter Yes/No)\n-> ")
                if play_again.lower() == "no":
                    show_score()
                    print("That's cool, have a good one! \nThank for playing, come play again!")
                    break
            elif int(your_guess) > random_number:
                print("It's lower.")
                attempts += 1
            elif int(your_guess) < random_number:
                print("It's higher.")
                attempts += 1
        except ValueError as err:
            print("Oh no!, that is not a valid value. Try again...")
            print("({})".format(err))
    else:
        show_score()
        print("Come play again.")
if __name__ == '__main__':
    start_game()
