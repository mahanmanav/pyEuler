'''
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''


# Give: n < d and i ∈ N we have equation d(10n+i) = n(10i+d) which give: n < d < i:

nProd = dProd = 1
for i in range(1, 10):
    for d in range(1, i):
        for n in range(1, d):
            if(d*(10*n+i) == n*(10*i+d)):
                nProd *= n
                dProd *= d    
                
# reduce to simplest form
def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

result = int(dProd/gcd(nProd, dProd)) 
print(result)