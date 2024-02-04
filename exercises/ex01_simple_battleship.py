"""EX01 - Simple Battleship - A cute step toward Battleship."""

__author__ = "730396719"

# Player 1's Input
location = int(input("Pick a secret boat location between 1 and 4: "))
if location < 1: 
    print(f"Error! {location} too low!") 
    exit()
if location > 4: 
    print(f"Error! {location} too high!")
    exit()


# Player 2's Input 
location_guess = int(input("Guess a number between 1 and 4: "))
if location_guess < 1: 
    print(f"Error! {location_guess} too low!")
    exit()
if location_guess > 4: 
    print(f"Error! {location_guess} too high!")
    exit()


# Do they match?
if location_guess == location:
    print("Correct! You hit the ship.")
else: 
    print("Incorrect! You missed the ship.")

# String of boxes 
BLUE_BOX: str = "\U0001F7E6"
RED_BOX: str = "\U0001F7E5"
WHITE_BOX: str = "\U00002B1C"

emoji: str = ""

if location_guess == location:
    result = RED_BOX
else:
    result = WHITE_BOX

if location_guess == 1:
    emoji += result
else:
    emoji += BLUE_BOX

if location_guess == 2:
    emoji += result
else:
    emoji += BLUE_BOX

if location_guess == 3:
    emoji += result
else:
    emoji += BLUE_BOX

if location_guess == 4:
    emoji += result
else:
    emoji += BLUE_BOX

print(emoji)

if result == RED_BOX:
    print("Correct! You hit the ship.")
else: 
    print("Incorrect! You missed the ship.")