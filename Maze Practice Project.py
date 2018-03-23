maze = [["_", "_", "_", "W"],
        ["_", "W", "_", "_"],
        ["_", "W", "W", "_"]]

start_row = 2
start_col = 0

end_row = 2
end_col = 3

def get_maze_contents(row, col):
    if row == end_row and col == end_col:
        return "E"
    elif row == start_row and col == start_col:
        return "S"
    else:
        return maze[row][col]

def pretty_print_maze(player_row, player_col):
    for row_index in range(0, len(maze)):
        pretty_row = ""
        for col_index in range(0, len(maze[0])):
            if row_index == player_row and col_index == player_col:
                pretty_row += "P "
            else:
                pretty_row += get_maze_contents(row_index, col_index) + " "
        print(pretty_row)

def is_valid_move(player_row, player_col, direction):
    next_row = player_row
    next_col = player_col
    if direction == "up":
        next_row -= 1
    elif direction == "down":
        next_row += 1
    elif direction == "left":
        next_col -= 1
    elif direction == "right":
        next_col += 1
    if next_row < 0 or next_row >= len(maze):
        print("That is not a valid move.")
        return False
    elif next_col < 0 or next_col >= len(maze[next_row]):
        print("That is not a valid move.")
        return False
    next_space_contents = get_maze_contents(next_row, next_col)
    if next_space_contents == "W":
        print("That is not a valid move.")
        return False
    else:
        return True

def move(player_row, player_col, direction):
    new_player_row = player_row
    new_player_col = player_col
    if is_valid_move(player_row, player_col, direction):
        if direction == "up":
            new_player_row -= 1
        elif direction == "down":
            new_player_row += 1
        elif direction == "left":
            new_player_col -= 1
        elif direction == "right":
            new_player_col += 1
    else:
        return [player_row, player_col]
    return [new_player_row, new_player_col]

def play_game():
    player_row = start_row
    player_col = start_col
    while True:
        pretty_print_maze(player_row, player_col)
        if player_row == end_row and player_col == end_col:
            print("You made it!")
            break
        direction = input("Enter your direction of movement.")
        new_player_loc = move(player_row, player_col, direction)
        player_row = new_player_loc[0]
        player_col = new_player_loc[1]
# Only show part of the maze
# Loading a maze from a file
# Add graphics
# Door and key

play_game()

def am_I_alive():
    print("orangutan")
    x = input("Enter the word you see above.")
    if x == "orangutan":
        print("You are alive!")

am_I_alive()
