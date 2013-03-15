'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! 
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)
'''

tData = ([])
index = 0
file = open("../resource/pr67Data.txt")
for line in file:
    tData.append([])
    numbers = line.split()
    for num in numbers:
        tData[index].append(int(num))
    index += 1

import copy
mData = copy.deepcopy(tData)

for i in range(1, len(tData)):
    route = tData[i]
    for j in range(len(route)):
        if(j == 0):
            tData[i][j] += tData[i-1][j]
            continue;
        if(j == (len(route)-1)):
            tData[i][j] += tData[i-1][j-1]
            continue;
        else:
            tData[i][j] += max(tData[i-1][j-1], tData[i-1][j])     
    
jval = tData[len(tData)-1].index(max(tData[len(tData)-1]))

#iterate through tData and for every highest value in upward direction add value to result in original structure
result = mData[len(mData)-1][jval]
for i in range(len(mData)-2, -1, -1):
    if((jval-1) < 0):
        result += mData[i][jval]
        continue;
    if(jval == len(tData[i])):
        jval = jval - 1
        result += mData[i][jval]
        continue;
    else:
        if(tData[i][jval-1] > tData[i][jval]):
            result += mData[i][jval-1]
            jval -= 1
        else:
            result += mData[i][jval]
               
print(result)