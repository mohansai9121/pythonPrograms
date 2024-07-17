# Tic Tac Toe game implementation in Python
squares = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
player = 'X'
running = 1


def board():
    print()
    print(squares[0], end="|")
    print(squares[1], end="|")
    print(squares[2])
    print('--- --- ---')
    print(squares[3], end="|")
    print(squares[4], end="|")
    print(squares[5])
    print("--- --- ---")
    print(squares[6], end="|")
    print(squares[7], end="|")
    print(squares[8])


def check_winner():
    if squares[0] == squares[1] == squares[2] and squares[0] != "   ":
        return 0
    elif squares[3] == squares[4] == squares[5] and squares[3] != "   ":
        return 0
    elif squares[6] == squares[7] == squares[8] and squares[8] != "   ":
        return 0
    elif squares[0] == squares[3] == squares[6] and squares[3] != "   ":
        return 0
    elif squares[1] == squares[4] == squares[7] and squares[1] != "   ":
        return 0
    elif squares[2] == squares[5] == squares[8] and squares[8] != "   ":
        return 0
    elif squares[0] == squares[4] == squares[8] and squares[0] != "   ":
        return 0
    elif squares[2] == squares[4] == squares[6] and squares[2] != "   ":
        return 0
    elif squares[0] != "   " and squares[1] != "   " and squares[2] != "   " and squares[3] != "   " and squares[4] != "   " and squares[5] != "   " and squares[6] != "   " and squares[7] != "   " and squares[8] != "   ":
        return -1
    else:
        return 1


print("This is Tic-Tac-Toe game board")
board()
print("Please choose positions from \'1\' to \'9\' only")
print("There are two markings: \'X\' and \'O\'")
player1 = input('Name of player(playing for \'X\'):')
player2 = input('Name of player(playing for \'O\'):')
print("Start playing...")
while running == 1:
    if player == 'X':
        print(f'{player1}\'s turn', end=',')
        box = int(input("enter position:"))
        while box > 9 or box < 1:
            box = int(input(f"{player1}, Choose between 1 and 9:"))
        while squares[box-1] != "   ":
            box = int(input("Already filled, choose other position:"))
        squares[box-1] = " X "
        player = 'O'
    else:
        print(f'{player2}\'s turn', end=",")
        box = int(input("enter position:"))
        while box > 9 or box < 1:
            box = int(input(f"{player2}, Choose between 1 and 9:"))
        while squares[box-1] != "   ":
            box = int(input("Already filled, choose other position:"))
        squares[box-1] = " O "
        player = 'X'
    board()
    running = check_winner()
if running == 0:
    if player == 'O':
        print(f"{player1} is the winner...!")
    else:
        print(f"{player2} is the winner...!")
else:
    print("game draw...!")
