'''
The number 3797 has an interesting property. 
Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

# 6 digit prime number should be enough to generate 11 primes
sieve = [True] * 1000000
for i in range(2, int(len(sieve)/2)):
    for j in range(2*i, len(sieve), i):
        sieve[j] = False
        
primes = set(str(i) for i in range(2, len(sieve)) if sieve[i])

result = 0
for prime in primes:
    count = 1
    for i in range(len(prime)):
        if((prime[i+1:] not in primes) or (prime[:-i-1] not in primes)):
            break;
        count += 1
    
    if(len(prime) > 1 and count == len(prime)):
        result += int(prime)
  
print(result)