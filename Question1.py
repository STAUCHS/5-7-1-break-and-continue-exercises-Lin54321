#-------------------------------------------------------------------------
# Name:       Question #1
# Purpose:    A loop that outputs numbers from 0 to 10, but skips number 7
# Author:     Lin. H
# Created:    06/05/2024
#-------------------------------------------------------------------------

n = 0

while n < 11:
    if n == 7:
        n += 1
        continue
    print(n)
    n += 1