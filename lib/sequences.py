#!/usr/bin/env python3


s = [2,6,3,9,3,4,6]

ele = s[len(s)-2:len(s)+1]

print(ele)

my_range = range(2,10,2)
print(my_range)
# => range(0, 4)

fibonacci_nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89,144,233]

def print_fibonacci(length):
    print(fibonacci_nums[0:length])
    pass

print(print_fibonacci(9))