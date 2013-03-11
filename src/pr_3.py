'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

inVal = 600851475143

count = 2
while ( count * count < inVal):
    while(inVal%count == 0):
        inVal = inVal/count
    count+=1

print(int(inVal));
