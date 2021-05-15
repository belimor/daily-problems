#!/usr/bin/python3
# 
# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3

def lowest_number(numbers):
    print(numbers)
    new_numbers = [];
    for i in range(len(numbers)):
        if numbers[i] > 0:
            new_numbers.insert(i,numbers[i])
    print(new_numbers)
    j = 0
    found_number = False
    while not found_number:
        j += 1
        if j not in new_numbers:
            found_number = True
        else:
            found_number = False
    print("Lowest number: " + str(j))

lowest_number([3,4,-1,1])
lowest_number([1,2,0])
lowest_number([10,9,8,7,6,5,3,4,2,1])

