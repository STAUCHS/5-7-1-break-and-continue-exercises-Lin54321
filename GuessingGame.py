#-------------------------------------------------------------------------
# Name:       Guessing game
# Purpose:    User guesses a number between 1 and 100 with only 5 tries
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

import random

# Output title
print("*** Guess the Number ***")
print("Welcome to the guess the number game.")
print("You have 5 chances to guess the number between 1 and 100.\n")

# Generate random number between 1 and 100
num = random.randrange(1, 101)

# Intialize variable
tries = 1

# When guess is incorrect 
while True:
  guess = int(input("Enter a number between 1 and 100: "))
  if guess > num and tries < 5:
    print("Too high, guess again\n")
    tries += 1
  elif guess < num and tries < 5:
    print("Too low, guess again\n")
    tries += 1
  elif guess == num or tries >= 5:
    break

# Output message when guess is correct
if tries < 5:
    print("\nCongratulations! You guessed correct!")

# Output message when guess is incorrect and number of tries is used up
else:
    print(f"\nSorry, you've guessed incorrectly, the number is {num}.")