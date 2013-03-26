'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 x 1 = 192
192 x 2 = 384
192 x 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, 
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

'''
Trials:
9 1,2 = 918 (3 digit)
98 1,2 = 98196 (5 digit)
987 1,2 = 9871974 (7 digit)
9876 1,2 = 987619752 (9 digit)

9 1,2,3 = 91827 (5 digit)
98 1,2,3 = 98196294 (8 digit)
987 1,2,3 = 98719742961 (11-digit)

91 1,2 = 91182 (5 digit)
912 1,2 = 9121824 (7 digit)
9123 1,2 = 912318246 (9 digit)

91 1,2,3 = 91182273 (8-digit)
912 1,2,3 = 91218242736 (11-digit)

So range must be 9123-9876
'''

for i in range(9876, 9122, -1):
    num = str(i) + str(i*2)
    panD = True
    for j in range(1, 10):
        if str(j) not in num:
            panD = False
    if panD:
        print(num)
        break;