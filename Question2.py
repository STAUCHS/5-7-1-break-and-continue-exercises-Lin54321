#-------------------------------------------------------------------------
# Name:       Question #2
# Purpose:    A loop that will add the numbers from 5 to 20, but not any multiples of 3
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

n = 5
total = 0

while n < 21:
    if n % 3 == 0:
        n += 1
        continue
    total += n
    n += 1

print(total)