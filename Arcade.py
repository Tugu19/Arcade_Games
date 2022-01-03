from Ascii import arcadeLogo
import os
from XandO import Xando
from Hangman import HangGame
from RockPaperScissors import RPSGame
from BlackJack import Black_Jack
from Dices import DiceGame
from Treasure import Treasure2
from Rules import GameRules

while True:
    os.system('cls')
    print(arcadeLogo)
    print("Welcome to Ascii arcade game")
    print("Press the corresponding number for the game\n")
    print("""
    1. Tic Tac Toe 
    2. Rock, paper, scissors
    3. Hangman
    4. Treasure Island
    5. Dices 
    6. BlackJack
    7. Games Rules
    8. Exit
    """)
    x = input("Which game you want to play?  > ")
    if x == "1":
        Xando()
    elif x == "2":
        RPSGame()
    elif x == "3":
        HangGame()
    elif x == "4":
        Treasure2()
    elif x == "5":
        DiceGame()
    elif x == "6":
        Black_Jack()
    elif x == "7":
        GameRules()
    elif x == "8":
        break
    else:
        print("Unknown command. Try again")
