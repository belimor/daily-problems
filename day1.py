#!/usr/bin/python3
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

# Solution 1
def my_magic_number(numbers, magic_number):
    for index1, y in enumerate(numbers):
        for index2, x in enumerate(numbers):
            print(x + y)
            if index1 != index2 and x + y == magic_number:
                print("===================")
                print("Magic number is " + str(magic_number))
                return True
    print("===================")
    return False

print(my_magic_number([10, 15, 3, 7],17))

# Solution 2

def my_k_sum(numbers,k):
    stack = set ()
    for i, y in enumerate(numbers):
        if k - y in stack:
            return True
        stack.add(y)
        print(stack)
    return False

print(my_k_sum([10,15,3,7],17))
