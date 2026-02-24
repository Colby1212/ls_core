# Write a function that takes a list of numbers
# returns the sum of the sums of each leading subsequence in that list

# input --> list of numbers
# output --> number 

# Rules --> sum of the leading subsequences

# test cases: 

# The argument is [3, 5, 2].
# The sums of the leading subsequences are:
# 3
# 3 + 5 = 8
# 3 + 5 + 2 = 10
# The final result is 3 + 8 + 10 = 21.
# print(sum_of_sums([3, 5, 2]) == 21)

# The argument is [1, 5, 7, 3].
# The sums are:
# 1
# 1 + 5 = 6
# 1 + 5 + 7 = 13
# # 1 + 5 + 7 + 3 = 16
# # The final result is 1 + 6 + 13 + 16 = 36.
# print(sum_of_sums([1, 5, 7, 3]) == 36)

# print(sum_of_sums([4]) == 4)
# print(sum_of_sums([1, 2, 3, 4, 5]) == 35)



# data types --> list, number

# Algorithm
# iterate over each index of the list.
# at each index, sum the elemeents from teh start to the list to that index
# store the sum 
# total the sums
# return the total

# Code

def sum_of_sums(numbers):
    total = 0
    for index in range(len(numbers)):
        total += sum(numbers[:index +1])
    return total

print(sum_of_sums([1, 5, 7, 3]) == 36)

print(sum_of_sums([4]) == 4)
print(sum_of_sums([1, 2, 3, 4, 5]) == 35)