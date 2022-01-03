from Ascii import ruleTitle
import os

def GameRules():

    os.system('cls')
    print(ruleTitle)
    print("Welcome to rules. On this window you have the rules for all games.")
    print("\n")
    print("""1. Tic, Tac, Toe
    Tic-tac-toe is played on a three-by-three grid by two players, who alternately place the marks X and O in one of the nine spaces in the grid.  
    There is no universally-agreed rule as to who plays first, but the convention that X plays first is used.
    In this program you must put two numbers without spaces (eg. 12, 11, 21, 23) to fill the position you want to choose.
    If you type the place wrong, or the place is already taken, the program will tell you that""")