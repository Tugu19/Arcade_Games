import random
from Ascii import hang
from Ascii import hangTitle
import os

def HangGame():
    os.system('cls')
    print(f"{' '.join(hangTitle)}")
    file = open("Words", "r")
    words = file.readline()

    word_list = words.split('","')
    while True:

        ok = 0
        game_word = random.choice(word_list)
        used_letter = []
        lives = 6
        display = []
        len_game_word = len(game_word)

        for i in range(len_game_word):
            display += '_'

        print(f"    {' '.join(display)}")
        print(hang[6])

        while lives > 0:

            letter = input("    Guess a letter: ")

            if letter >= 'A' and letter <= 'Z':
                print("    All letters are lowercase\n")
                continue

            if letter < 'a' or letter > 'z':
                print("    This is not a letter, try again.\n")
                continue


            if letter in used_letter:
                print("    The letter is already used.\n")
                continue
            os.system('cls')
            if letter not in game_word:
                lives -= 1
                print(f"    {' '.join(display)}")
                print(hang[lives])
                used_letter += letter
                print(f"    Used letters: {', '.join(used_letter)}")
            else:
                for pos in range(len_game_word):
                    if letter == game_word[pos]:
                        display[pos] = letter
                print(f"    {' '.join(display)}")
                print(hang[lives])
                used_letter += letter
                print(f"    Used letters: {', '.join(used_letter)}")
            if '_' not in display:
                lives = -1
                print("       You won\n")
                again = input("   Do you want to play again?(y for yes, n for no) > ")
                ok = 1


        if ok == 0:
            print(f"You lost. The word was: {game_word}")
            again = input("Do you want to play again?(y for yes, n for no) > ")

        os.system('cls')

        if again == "n":
            os.system('cls')
            return 0