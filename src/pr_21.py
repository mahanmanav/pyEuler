'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

amSet = set()
for amNum in range(1, 10000):
    sumA = sum(i for i in range(1, amNum) if(amNum%i == 0))
    if(sumA != amNum):
        sumB = sum(j for j in range(1, sumA) if(sumA%j == 0)) 
        if(amNum == sumB):
            amSet.add(sumA)
            amSet.add(sumB)

print(sum(amSet))