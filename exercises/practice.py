grid_size = 4
secret_row = 3
secret_column = 2

valid_input = False
while not valid_input:
    guess_row = int(input("Guess a row: "))
    if 0 < guess_row <= grid_size:
            valid_input = True
    else:
            print(f"The grid is only {grid_size} by {grid_size}. Try again.")

valid_input = False
while not valid_input:
    guess_column = int(input("Guess a column: "))
    if 0 < guess_column <= grid_size:
            valid_input = True
    else:
            print(f"The grid is only {grid_size} by {grid_size}. Try again.")

if guess_row == secret_row and guess_column == secret_column:
    print("Hit!")
else:
    print("Miss!")