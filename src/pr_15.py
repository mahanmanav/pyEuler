'''
Starting in the top left corner of a 2X2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20X20 grid?
'''

gSize = 20
#calculate nCk value e.g. 4c2 = 6
nVal = 2* gSize
kVal = gSize

result = 1
while(kVal > 0):
    result = (result * nVal)/kVal
    nVal, kVal = nVal-1, kVal-1

print(round(result))

