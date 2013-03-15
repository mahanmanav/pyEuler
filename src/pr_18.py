'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; 
it cannot be solved by brute force, and requires a clever method! ;o)
'''

tData = ([])
index = 0
file = open("../resource/pr18Data.txt")
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