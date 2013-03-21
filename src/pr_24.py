'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''

# http://en.wikipedia.org/wiki/Factorial_number_system
# There is a natural mapping between n digits in factorial representation and permutation of n elements in lexicographical order

position = 1000000-1

fMap = {0:1}
for i in range(1, 10):
    fMap[i] = fMap[i-1] * i

factoradic = []
for i in range(9, -1, -1):
    factoradic.append(int(position/fMap[i]))
    position = position%fMap[i]

dSet = list(i for i in range(10))
permutation = 0
for i in factoradic:
    permutation = (permutation * 10) + dSet[i] 
    dSet.remove(dSet[i])
    
print(permutation)    