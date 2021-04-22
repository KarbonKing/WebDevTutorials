import os
# ///// Global Variables \\\\\\


#Game Board
board = ['-', '-', '-','-', '-', '-', '-', '-', '-']

# If game is still going
game_still_going = True


#Winner/Tie
winner = None


#Whose turn is it?
current_player = "X"


# The screen clear function
def screen_clear():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')



def display_board():
    print(board[0] + " | " +board[1]+ " | " +board[2])
    print(board[3] + " | " +board[4]+ " | " +board[5])
    print(board[6] + " | " +board[7]+ " | " +board[8])


#Handle a single turn for an arbitrary player
def handle_turn(player):
    print("")
    print(player + "'s turn..")
    
    position = input("\nChoose a position from 1-9: ")
    
    valid = False
    while not valid:
        while position not in ["1","2","3","4","5","6","7","8","9"]:
            screen_clear()
            display_board()
            print("")
            print(player + "'s turn..")
            position = input("\nInvalid Input Dude o_O \nChoose a position from 1-9: ")
        
        position = int(position) -1
        if board[position] == "-":
            valid = True
    
    board[position] = player
    screen_clear()
    display_board()



def play_game():
    screen_clear()
    
    #Displaying Initial Board
    display_board()
    
    while game_still_going:
    
        #Handle a single turn of the player
        handle_turn(current_player)
    
        check_if_game_over()
    
        #Flip to the other player
        flip_player()

    #The Game has ended
    if winner == "X" or winner == "O":
        print("" * 10)
        print(winner + " Won! ^_^\n")
    elif winner == None:
        print("" * 10)
        print("Tie -_-\n")





def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    #setup global variables
    global winner
    #check rows
    row_winner = check_rows()
    #check columns
    column_winner = check_columns()
    #check diagonlas
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None

    return



def check_rows():
    #Setup Global Variables
    global game_still_going

    #Check if any rows have the same value (and is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    #If any row matches, flag that there is a win
    if row_1 or row_2 or row_3:
        #End Game
        game_still_going = False

    #Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    #Setup Global Variables
    global game_still_going

    #Check if any columns have the same value (and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    #If any column matches, flag that there is a win
    if column_1 or column_2 or column_3:
        #End Game
        game_still_going = False

    #Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    #Setup Global Variables
    global game_still_going

    #Check if any diagonals have the same value (and is not empty)
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[6] == board[4] == board[2] != "-"

    #If any diagonal matches, flag that there is a win
    if diagonal_1 or diagonal_2:
        #End Game
        game_still_going = False

    #Return the winner (X or O)
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False

    return

def flip_player():
    #Pulling Global Variable
    global current_player

    #if the current player is X then change it to O
    if current_player == "X":
        current_player = "O"

    #if the current player is O then change it to X
    elif current_player == "O":
        current_player = "X"
    return

play_game()

