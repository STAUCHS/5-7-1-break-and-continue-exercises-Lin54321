#-------------------------------------------------------------------------
# Name:       Bank PIN
# Purpose:    Checks the user has entered the correct 4-digit PIN so they can access their account
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

# Output title
print("WELCOME TO STA BANK!")

# Intialize correct PIN
correct_PIN = 1938

# Get PIN from user and reprompt when PINs don't match
while True:
  entered_PIN = int(input("\nEnter your PIN: "))
  if entered_PIN != correct_PIN:
    print("Incorrect PIN. Try again.")
  else:
    break

# Output message when PIN is correct
print("PIN accepted. You may now access your account.")