'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

limit = 20
def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

def lcd(x, y):
    return int((x*y/gcd(x,y)))
    
result = 1           
for i in range(1, limit):
    result = lcd(result, i)
    
print(result)