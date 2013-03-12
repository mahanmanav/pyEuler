'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

''''
http://en.wikipedia.org/wiki/Pythagorean_triple
a=m^2 - n^2; b=2mn; c=m^2+n^2 with a+b+c = 1000 we get equation m(m+1)=500
'''

for n in range(1000):
    for m in range(n, 1000):
        a = m*m - n*n
        b = 2*m*n
        c = m*m + n*n
        if(a+b+c == 1000):
            print(a*b*c)