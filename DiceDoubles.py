#-------------------------------------------------------------------------
# Name:       Dice doubles
# Purpose:    Simulates dice rolls until the dice show doubles
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

import random

# Output title
print("HERE COMES THE DICE!")

# Simulates dice roll until dice rolls are the same and output results
while True:
    roll_one = random.randrange(1, 7)
    roll_two = random.randrange(1, 7) 
    total = roll_one + roll_two

    print(f"\nRoll #1: {roll_one}")
    print(f"Roll #2: {roll_two}")
    print(f"The total is {total}!")
    if roll_one == roll_two:
        break