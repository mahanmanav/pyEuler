'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

limit = 2000000
def slow_version():
    result, number, primes = 2, 2, [2]
    while(number < limit):
        if(number%2 != 0):
            flag = True
            for prime in primes:
                if(number%prime==0):
                    flag = False
                    break
            if(flag):
                result += number
                primes.append(number)
        number += 1
    print(result)

def fast_version():
    sieve = [True] * limit
    
    for i in range(2, int(len(sieve)/2)):
        for j in range(i*2, len(sieve), i):
            sieve[j] = False
            
    print(sum(i for i in range(2, len(sieve)) if sieve[i]))

fast_version()