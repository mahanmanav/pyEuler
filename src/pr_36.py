'''
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''

total = 0
for num in range(1, 1000000):
    if(str(num) == (str(num)[::-1])):
        if(bin(num)[2:] == ((bin(num)[2:])[::-1])):
            total += num

print(total)