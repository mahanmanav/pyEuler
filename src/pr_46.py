'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2x1^2
15 = 7 + 2x2^2
21 = 3 + 2x3^2
25 = 7 + 2x3^2
27 = 19 + 2x2^2
33 = 31 + 2x1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''

# limit = 10000 just a sufficiently large number figured out after trial
from math import sqrt

limit = 10000 
sieve = [True] * limit
for i in range(2, int(len(sieve)/2)):
    for j in range(i*2, len(sieve), i):
        sieve[j] = False

primes = list(i for i in range(2, len(sieve)) if sieve[i])

for num in range(9, limit, 2):
    cRep, index = False, 0
    while(primes[index] <= num):            
        if(sqrt((num-primes[index])/2).is_integer()):
            cRep = True
            break
        
        index += 1
    if(not cRep):
        print(num)
        break