'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

start, end = 100, 1000
array = list(i*j for i in range(start, end) for j in range(start, end))
print(max(num for num in array if(num == int(str(num)[::-1]))))