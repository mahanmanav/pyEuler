'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000
'''

num = pow(2, 1000)
dSum = sum(int(i) for i in str(num))
print(dSum)