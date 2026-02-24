# create a function that takes a lsit of integers as an argument
# return the number of identical pairs of integers in that lsit

# input --> list of integers
# output --> # of identical pairs
# rules --> each number can only be used once 

# examples and test cases 

# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)


# Even empty lists return 0 and 1

# data types

# lists, integers

# Algorithm
# iterate over each number in the list and count the amoutn of time each number appears
# Sum the total of the values divided by 2 to find the amount of pairs that are in the list


# Code 

def pairs(numbers):
    return sum(numbers.count(num) // 2 for num in set(numbers))

print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)