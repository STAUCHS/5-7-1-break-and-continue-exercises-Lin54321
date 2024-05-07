#-------------------------------------------------------------------------
# Name:       Login
# Purpose:    Checks if username and password are correct
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

# Initialize correct username and password
correct_username = "StAugustineCHS"
correct_password = "Coding123!"

# Get username and password from user and determine if they are correct
while True:
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    if correct_username != entered_username and correct_password != entered_password:
        print("Username and password incorrect.\n")
    elif correct_username != entered_username:
        print("Username incorrect.\n")
    elif correct_password != entered_password:
        print("Password incorrect.\n")
    else:
        break

# Output message when username and password are correct
print("Welcome!")