#!/usr/bin/python3
#
# Given an array of integers: [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
# If our input was [3, 2, 1], the expected output would be [2, 3, 6].
# 

# Solution 1
def new_array(numbers):
    print(numbers)
    new_number = []
    for y in range(len(numbers)):
        sum = 1
        for x in range(len(numbers)):
            if x != y:
                sum = sum*numbers[x]
        new_number.insert(y, sum)
    print(new_number)
    print("===================")
    return True

new_array([1, 2, 3, 4, 5])

# Solution 2
import math

def my_new_array(numbers):
    print(numbers)
    new_number = []
    total = math.prod(numbers)
    for i in range(len(numbers)):
        new_number.insert(i, math.trunc(total/numbers[i]))
    print(new_number)
    print("===================")

my_new_array([1, 2, 3, 4, 5])

