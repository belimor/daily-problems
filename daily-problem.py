#!/usr/bin/env python3.7

#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

numbers = [10, 15, 3, 7]
magic_number = 17

# Solution 1
for index1, y in enumerate(numbers):
  for index2, x in enumerate(numbers):
    if index1 != index2:
      z = x + y
      print(str(x) + ' + ' + str(y) + ' = ' + str(z))
      if z == magic_number:
        print("yes")
      else:
        print("no")
    else:
      print("skip")
  print("===================")

# Solution 2
for i, y in enumerate(numbers):
    if magic_number - y in numbers:
        print("YES")
        print(y)
    else:
        print("NO")
