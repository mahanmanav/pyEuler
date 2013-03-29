'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''

# Highest panDigital primes can consist only upto 1 to 7. (if doesn't have redundant digits)
# http://en.wikipedia.org/wiki/Pandigital_number

sieve = [True] * 10000000
for i in range(2, int(len(sieve)/2)):
    for j in range(i*2, len(sieve), i):
        sieve[j] = False
        
primes = list(str(i) for i in range(2, len(sieve)) if sieve[i] and len(str(i)) > 6)
for prime in primes[::-1]:
    pFlag = True
    for i in range(1, 8):
        if(str(i) not in prime):
            pFlag = False

    if(pFlag):
        print(prime)
        break;