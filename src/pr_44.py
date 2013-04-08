'''
Pentagonal numbers are generated by the formula, Pn=n(3n1)/2. The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70  22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk  Pj| is minimised; what is the value of D?
'''

#http://en.wikipedia.org/wiki/Pentagonal_number

from math import sqrt
def isPentagonal(num):
    val = sqrt(1 + 24*num)
    if(val%6 == 5):
        return True
    return False
    
found, resutl, i = False, 0, 1
while(not found):
    i += 1
    nextP = i*(3*i-1)/2
    for j in range(i-1, 0, -1):
        prevP = j*(3*j-1)/2
        if(isPentagonal(nextP-prevP) and isPentagonal(nextP+prevP)):
            result = nextP-prevP
            found = True
            break;
        
print(int(result))