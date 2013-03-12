'''
The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

limit = 100
sumOfSquare =int((limit* (limit+1) * ((2*limit)+1))/6)
sumOfNum = int((limit * (limit+1))/2)
squareOfSum = sumOfNum * sumOfNum
print(squareOfSum - sumOfSquare)

