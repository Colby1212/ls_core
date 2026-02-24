# create a function that takes a list of integers
# returns the number of identical pairs in that list

# if the list is empty or contains exactly one value, return 0

# examples

# print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
# print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
# print(pairs([]) == 0)
# print(pairs([23]) == 0)
# print(pairs([997, 997]) == 1)
# print(pairs([32, 32, 32]) == 1)
# print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)

# it does not count the same element twice

# data types

# input --> list of integers
# output --> integer(total number of identical pairs)


# algorithm
# create a variable that store the number of pairs in the list.
# Go through each number in the list  
# for each pair increment the count by 1. 
# After checking the numbers, return the variable storing the count
# if the list is empty or has only a single element inside 0 should be returned

def pairs(nums):
    running_count = 0
    for num in set(nums):
        count = nums.count(num) // 2
        running_count += count
    return running_count


print(pairs([3, 1, 4, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]) == 3)
print(pairs([2, 7, 1, 8, 2, 8, 1, 8, 2, 8, 4]) == 4)
print(pairs([]) == 0)
print(pairs([23]) == 0)
print(pairs([997, 997]) == 1)
print(pairs([32, 32, 32]) == 1)
print(pairs([7, 7, 7, 7, 7, 7, 7]) == 3)