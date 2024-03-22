"""EX03 Functional Battleship."""

__author__ = "730396719" 

import random 


def input_guess(grid_size: int, specification: str) -> int:
    """User guess for row and column."""
    assert specification == "row" or specification == "column"
    valid_input = False
    if specification == "row":
        guess = int(input("Guess a row: "))
    else:
        guess = int(input("Guess a column: "))
    while not valid_input:
        if 1 <= guess <= grid_size:
            valid_input = True
        else:
            guess = int(input(f"The grid is only {grid_size} by {grid_size}. Try again: "))
    return guess


BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"


def print_grid(grid_size: int, row_guess: int, column_guess: int, correct: bool) -> None:
    """Making grid and boxes."""
    row_counter_idx: int = 1

    while row_counter_idx <= grid_size:
        row_result = ""
        column_counter_idx: int = 1

        while column_counter_idx <= grid_size:
            if row_guess == row_counter_idx and column_guess == column_counter_idx:
                row_result += RED_BOX if correct else WHITE_BOX
            else:
                row_result += BLUE_BOX

            column_counter_idx += 1

        print(row_result)
        row_counter_idx += 1


def correct_guess(secret_row: int, secret_column: int, guess_row: int, guess_column: int) -> bool:
    """Is the guess the same as the actual spot."""
    return secret_row == guess_row and secret_column == guess_column


def main(grid_size: int, secret_row: int, secret_column: int) -> None:
    """This is the main function in which the game gives five attempts to guess correctly."""
    max_turns = 5
    turn = 0

    while turn < max_turns:
        turn += 1
        print(f"=== Turn {turn}/{max_turns} ===")
        row_guess = input_guess(grid_size, "row")
        column_guess = input_guess(grid_size, "column")
        hit = correct_guess(secret_row, secret_column, row_guess, column_guess)
        print_grid(grid_size, row_guess, column_guess, hit)
        if hit:
            print("Hit!")
            print(f"You won in {turn}/{max_turns} turns!")
            return
        else:
            print("Miss!")
    print(f"X/{max_turns} - Better luck next time!")


if __name__ == "__main__":
    grid_size: int = random.randint(3, 5)
    main(grid_size, random.randint(1, grid_size), random.randint(1, grid_size))