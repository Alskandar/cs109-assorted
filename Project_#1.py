##This piece of code allows two players to play a standard game of 3x3 Tic-Tac-Toe. Click "Run Module" in the Run menu above to play a game.  Choose 1 player to be Player 1 (X’s) and one to be Player 2 (O’s).  Player 1 will go first.  When it is your turn, select a space by entering a code from the following table:
##top left, left top         top middle, middle top         top right, right top
##middle left, left middle   middle middle, center          right middle, middle right
##bottom left, left bottom   bottom middle, middle bottom   bottom right, right bottom
##Entering anything else, or trying to take a space that has already been taken, will re-prompt the current player to choose a space.  The game will end when one player achieves 3 letters in a row, or when the board is full.


# The following lines set the starting board state and create a few necessary variables.
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]
victory = 0
spaces = 0

# This function determines whether the space the player wants to take is available.
def is_space_open(row, col):
    space = get_value(row, col)
    if space == "-":
        return True
    else:
        print("That space is not available")
        return

# This function translates the player's input into coordinates for use in other functions.
def find_coordinates(player_input):
# These values below are necessary for the loops in the game function to work and are never actually used.
    row = 7
    col = 7
    n= 0
    if player_input == "top left" or player_input == "left top":
        row = 0
        col = 0
        n = 1
    elif player_input == "middle left" or player_input == "left middle":
        row = 1
        col = 0
        n=1
    elif player_input == "bottom left" or player_input == "left bottom":
        row = 2
        col = 0
        n=1
    elif player_input == "top middle" or player_input == "middle top":
        row = 0
        col = 1
        n=1
    elif player_input == "center" or player_input == "middle middle":
        row = 1
        col = 1
        n=1
    elif player_input == "bottom middle" or player_input == "middle bottom":
        row = 2
        col = 1
        n=1
    elif player_input == "top right" or player_input == "right top":
        row = 0
        col = 2
        n=1
    elif player_input == "middle right" or player_input == "right middle":
        row = 1
        col = 2
        n=1
    elif player_input == "bottom right" or player_input == "right bottom":
        row = 2
        col = 2
        n=1
    else:
        print("Not a valid input.")
    coordinates = [row, col, n]
    return coordinates

# This function prints the board in a way that looks like a tic-tac-toe board.  Code created by Edward Pantridge. 
def pretty_print_board():
    for row_index in range(0, len(board)):
        pretty_row = ""
        for col_index in range(0, len(board[0])):
            pretty_row += get_value(row_index, col_index) + " "
        print(pretty_row)

# This function translates a set of coordinates into the space's contents.
def get_value(row, col):
    return board[row][col]

# The following two functions update the board by adding letters.
def enter_value_X(row, col, spaces):
    if is_space_open(row, col):
        board[row][col] = "X"
        spaces +=1.0
    pretty_print_board()
    return spaces

def enter_value_O(row, col, spaces):
    if is_space_open(row, col):
        board[row][col] = "O"
        spaces +=1.0
    pretty_print_board()
    return spaces

# This function checks whether any player has three letters in a row, and ends the game if they do.
def win_cond(victory):
    if board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O":
        print("Player 2 wins!")
        victory +=1.0
    elif board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O":
        print("Player 2 wins!")
        victory +=1.0
    elif board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        victory +=1.0
    elif board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O":
        print("Player 2 wins!")
        victory +=1.0
    elif board[0][1] == "O" and board[1][1] == "O" and board[2][1] == "O":
        print("Player 2 wins!")
        victory +=1.0
    elif board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        victory +=1.0
    elif board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O":
        print("Player 2 wins!")
        victory +=1.0
    elif board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O":
        print("Player 2 wins!")
        victory +=1.0
    if board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X":
        print("Player 1 wins!")
        victory +=1.0
    elif board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X":
        print("Player 1 wins!")
        victory +=1.0
    elif board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        victory +=1.0
    elif board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X":
        print("Player 1 wins!")
        victory +=1.0
    elif board[0][1] == "X" and board[1][1] == "X" and board[2][1] == "X":
        print("Player 1 wins!")
        victory +=1.0
    elif board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        victory +=1.0
    elif board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X":
        print("Player 1 wins!")
        victory +=1.0
    elif board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X":
        print("Player 1 wins!")
        victory +=1.0
    return victory

# This is the overall function for the game.
def play_game():
    victory = 0
    spaces = 0
    turns = 0
    while True:
# This loop repeats until the player puts a letter in an allowed space.
        while spaces == 0:
            n=0
# This loop repeats until the player types in a code for a space on the board.
            while n == 0:
                player_input = input("Player 1, enter your space.")
                coordinates = find_coordinates(player_input)
                n = coordinates[2]
            row = coordinates[0]
            col = coordinates[1]
            spaces = enter_value_X(row, col, spaces)
        victory = win_cond(victory)
        spaces = 0
        if victory == 1:
            return
        turns += 1
# The if-then statement below ends the game once the board is full.
        if turns >= 9:
            print("The game is tied.")
            return
# This code below is a copy of the above code, but enters a letter for Player 2 instead.
        while spaces == 0:
            n = 0
            while n == 0:
                player_input = input("Player 2, enter your space.")
                coordinates = find_coordinates(player_input)
                n = coordinates[2]
            row = coordinates[0]
            col = coordinates[1]
            spaces = enter_value_O(row, col, spaces)
        victory = win_cond(victory)
        spaces = 0
        if victory == 1:
            return
        turns += 1

play_game()
