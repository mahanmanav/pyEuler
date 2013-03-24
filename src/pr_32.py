'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

# product of a < 100 and b < 1000 will form 4 digit n (2 + 3 + 4 = 9 digit)
pSet = set()
for i in range(1, 100):
    for j in range(100, 10000):
        prod = i * j
        if(prod not in pSet):
            tStr = "".join(sorted(str(i) + str(j) + str(prod)))
            if(tStr == "123456789"):
                pSet.add(prod)

print(sum(pSet))