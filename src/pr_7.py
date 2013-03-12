'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''

limit = 10001
number, primes = 2, [2]

while(len(primes) < limit):
    if(number%2 != 0):
        flag = True
        
        for prime in primes:
            if(number%prime == 0):
                flag = False
                break
            
        if(flag):
            primes.append(number)
    number += 1
    
print(primes[limit-1])
