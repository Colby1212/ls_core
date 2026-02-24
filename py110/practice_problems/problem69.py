# create a function that takes a list of integers as an argument and returns the integer that appears an odd number of times
# There will always be exactly on such integer in the input list


# input --> list of numbers
# output --> the number appears an odd number of times

# There will only ever be one integer that appears an odd number of times in the list



# examples and test cases 

# print(odd_fellow([4]) == 4)
# print(odd_fellow([7, 99, 7, 51, 99]) == 51)
# print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
# print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
# print(odd_fellow([0, 0, 0]) == 0)



# data types
# dictionaries , Integers




# Algorithm

# Iterate over list of numbers, count hte number of times each appears in teh list
# If one appears an odd amount of times return that number

# Code 


def odd_fellow(numbers):
    for num in set(numbers):
        if numbers.count(num) % 2 == 1:
            return num

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)

def odd_fellow(numbers):
    count = {}
    for num in numbers:
        count[num] = count.get(num, 0) + 1
    for num in count:
        if count[num] % 2 == 1:
            return num 
        
print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)