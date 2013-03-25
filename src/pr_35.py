'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''

sieve = [True] * 1000000
for i in range(2, int(len(sieve)/2)):
    for j in range(i*2, len(sieve), i):
        sieve[j] = False
        
primes = set(i for i in range(2, len(sieve)) if sieve[i])

count = 0
for prime in primes:
    temp = 0
    for i in range(len(str(prime))):
        prime = str(prime)[1:]+str(prime)[0]
        if(int(prime) in primes):
            temp += 1
    
    if(temp == len(str(prime))):
        count += 1

print(count)