'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
'''

'''
http://en.wikipedia.org/wiki/Pythagorean_triple
For m > n
a = m^2 - n^2
b = 2mn
c = m^2 + n^2
'''

import math

limit = 1001
pDict = dict()
for a in range(1, limit):
    for b in range(1, limit):
        c = math.sqrt((a*a) + (b*b))
        p = a + b + c
        if(p < limit):
            if(p in pDict):
                pDict[p] = pDict.get(p) + 1
            else:
                pDict[p] = 1

key = max = 0
for k, v in pDict.items():
    if(v > max):
        key, max = k, v

print(key)