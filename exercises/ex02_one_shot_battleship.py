"""EX02 - One Shot Battleship."""

__author__ = "730396719"

# Battleship game setup location
grid_size = 4
secret_row = 3
secret_column = 2

# User guess for which row
valid_input = False
guess_row = int(input("Guess a row: "))
while not valid_input:
    if 0 < guess_row <= grid_size:
        valid_input = True
    else:
        guess_row = int(input((f"The grid is only {grid_size} by {grid_size}. Try again: ")))

# User guess for which column
valid_input = False
guess_column = int(input("Guess a column: "))
while not valid_input:
    if 0 < guess_column <= grid_size:
        valid_input = True
    else:
        guess_column = int(input((f"The grid is only {grid_size} by {grid_size}. Try again: ")))

# Making the grid and boxes for battleship
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

# Start with row 1 and index it till it goes to grid size and then stop the loop once bigger than grid size
row_counter_idx: int = 1

while row_counter_idx <= grid_size:
    row_result = ""
    column_counter_idx: int = 1

    while column_counter_idx <= grid_size:
        if guess_row == row_counter_idx and guess_column == column_counter_idx:
            row_result += RED_BOX if guess_row == secret_row and guess_column == secret_column else WHITE_BOX
        else:
            row_result += BLUE_BOX

        column_counter_idx += 1

    print(row_result)
    row_counter_idx += 1

# Hit or miss or close guess at bottom
if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
elif guess_row == secret_row and guess_column != secret_column:
    print("Close! Correct row, wrong column.")
elif guess_row != secret_row and guess_column == secret_column:
    print("Close! Correct column, wrong row.")
else:
    print("Miss!")