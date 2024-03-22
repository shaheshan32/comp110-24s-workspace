"""Number Guessing Game"""
from random import randint

SECRET: int = randint(1,10)
correct: bool = False 

while not correct: #or say correct == False 
    guess: int = int(input("Guess a number:"))
    if guess == SECRET:
        print("You got it right" + str(guess) + "is the secret number!")
        print(f"You got it right! {guess} is the secret number!")
        correct = True
    else:
        if guess < SECRET:
            print("your guess was too low, try again")
        if guess > SECRET:
            print("your guess was too high, try again")