'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
'''

fdict = {}
fdict['0'] = 1

for num in range(1, 10):
    fdict[str(num)] = num * fdict.get(str(num-1))
    
total, num, limit = 0, 10, fdict.get('9')
while(limit*len(str(num)) > num):
    dSum = 0
    for dig in str(num):
        dSum += fdict.get(dig)
    
    if(dSum == num):
        total += num
    
    num += 1
    
print(total)