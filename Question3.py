#-------------------------------------------------------------------------
# Name:       Question #3
# Purpose:    Ask user for starting and ending number and adds them up, except 13 or 31
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

sum = 0

starting_num = int(input("Enter starting number: "))
ending_num = int(input("Enter ending number: "))

while starting_num <= ending_num:
    if starting_num == 13:
        break
    if starting_num == 31:
        break
    sum += starting_num
    starting_num += 1

print(sum)