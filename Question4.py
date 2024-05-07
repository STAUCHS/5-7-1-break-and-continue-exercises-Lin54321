#-------------------------------------------------------------------------
# Name:       Question #4 
# Purpose:    Ask the user to enter a word indefinitely until they enter the word stop
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

while True:
    word = input("Enter a word: ")
    if word == "stop":
        break
    print(f"Your word: {word}\n")

print("Goodbye!")