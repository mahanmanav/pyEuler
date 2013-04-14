'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle         Tn=n(n+1)/2         1, 3, 6, 10, 15, ...
Pentagonal       Pn=n(3n1)/2         1, 5, 12, 22, 35, ...
Hexagonal        Hn=n(2n1)         1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''

from math import sqrt
def isPentagonal(num):
    val = sqrt(1+24*num)
    if(val%6==5):
        return True
    return False

def isHexagonal(num):
    val = sqrt(1+8*num)
    if(val%4==3):
        return True
    return False

ti = 285+1
while(True):
    tNum = int(ti*(ti+1)/2)
    if(isPentagonal(tNum) and isHexagonal(tNum)):
        print(tNum);
        break;
    ti += 1