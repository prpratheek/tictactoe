board =["-","-","-",
        "-","-","-",
        "-","-","-"]

game_on=True

winner=None

current_player="X"

def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])


def play_game():
    display_board()

    while game_on:
        handle_turn(current_player)

        check_game_over()

        flip_player()

    if winner=="X" or winner=="O":
        print(winner +" won!!!")
    elif winner==None:
        print("It's a tie")


def handle_turn(player):
    print(player+"'s turn.")
    position=input("Choose a position from 1-9: ")
    valid=False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            position=input("Invalid input. Choose a position from 1-9: ")

        position=int(position)-1

        if board[position] == "-":
            valid=True
        else:
            print("You can't override. Play again")

    board[position]=player
    display_board()


def check_game_over():
    check_win()
    check_tie()

def check_win():

    global winner
    #rows
    row_winner=check_rows()

    #columns
    column_winner=check_columns()

    #diagonals
    diagonal_winner=check_diagonals()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
        winner=None
    return

def check_tie():
    global game_on
    if "-" not in board:
        game_on=False

    return


def flip_player():

    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"
    return


def check_rows():
    global game_on

    row_1=board[0]==board[1]==board[2] != "-"
    row_2=board[3]==board[4]==board[5] != "-"
    row_3=board[6]==board[7]==board[8] != "-"
    
    if row_1 or row_2 or row_3:
        game_on=False

    if row_1:
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]
    return

def check_columns():
    global game_on

    col_1=board[0]==board[3]==board[6] != "-"
    col_2=board[1]==board[4]==board[7] != "-"
    col_3=board[2]==board[5]==board[8] != "-"
    
    if col_1 or col_2 or col_3:
        game_on=False

    if col_1:
        return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return

def check_diagonals():
    global game_on

    dia_1=board[0]==board[4]==board[8] != "-"
    dia_2=board[6]==board[4]==board[2] != "-"
    
    if dia_1 or dia_2:
        game_on=False

    if dia_1:
        return board[0]
    if dia_2:
        return board[6]

    return


play_game()