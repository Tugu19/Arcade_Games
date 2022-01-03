import os
from Ascii import ticTacTitle
def Xando():
    while True:
        os.system('cls')
        print(ticTacTitle)
        print("\n  Welcome to Tic Tac Toe!")
        print("  1. Play")
        print("  2. Back")
        game = int(input("  > "))
        os.system('cls')
        if game == 2:
            return 0
        row1 = ["*", "*", "*"]
        row2 = ["*", "*", "*"]
        row3 = ["*", "*", "*"]

        map = [row1, row2, row3]

        while game == 1:

            print(f"\n\n\n    {row1}\n    {row2}\n    {row3}\n")
            symbol = 1
            ok = 1

            while ok == 1:

                endGame = -1
                markPos = input("    which position you want to change? > ")

                if len(markPos) < 2:
                    print("    You missed a parameter")
                    continue

                if len(markPos) > 2:
                    print("    Unknown command. Try again\n")
                    continue

                if markPos[0] < '0' or markPos[0] > '9' or markPos[1] < '0' or markPos[1] > '9':
                    print("    Unknown command. Try again\n")
                    continue

                pos1 = int(markPos[0])
                pos2 = int(markPos[1])

                ctr = 0

                if map[pos1][pos2] == "*":
                    if symbol == 1:
                        map[pos1][pos2] = "X"
                        symbol = 0
                        ctr += 1
                    else:
                        map[pos1][pos2] = "O"
                        symbol = 1
                        ctr += 1
                    endGame += 1
                else:
                    print("    This position is already occupied")

                if ctr == 9:
                    ok = 0
                os.system('cls')
                print(f"\n\n\n    {row1}\n    {row2}\n    {row3}\n")

                if map[0][0] == map[1][1] == map[2][2] != "*" or map[0][2] == map[1][1] == map[2][0] != "*" or map[0][0] == map[0][1] == map[0][
                    2] != "*" or map[1][0] == map[1][1] == map[1][2] != "*" or map[2][0] == map[2][1] == map[2][2] != "*" or map[0][0] == map[1][0] == \
                        map[2][0] != "*" or map[0][1] == map[1][1] == map[2][1] != "*" or map[0][2] == map[1][2] == map[2][2] != "*":
                    ok = 0
                    if symbol == 1:
                        print("    O won")
                    else:
                        print("    X won")
                    again = input("  Do you want to play again? (y for yes, n for no) > ")


            if endGame == 9:
                print("    It's a draw!")
                again = input("  Do you want to play again? (y for yes, n for no) > ")

            if again == "n":
                os.system('cls')
                game = 0
            else:
                os.system('cls')
                row1 = ["*", "*", "*"]
                row2 = ["*", "*", "*"]
                row3 = ["*", "*", "*"]
                map = [row1, row2, row3]