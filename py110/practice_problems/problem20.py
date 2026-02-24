# create a function that takes a list of numbers
# all of which are the same except one.
# find and return the number in the list that differs from the returns
# The list will always contain at least 3 numbers, there will always be exactly one number that is different


# input --> list of numbers
# output --> The only unique number in that list

# Rules --> The list will always contain at least 3 numbers, there will always be exactly one number that is different

# examples 

# print(what_is_different([0, 1, 0]) == 1)
# print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
# print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
# print(what_is_different([3, 4, 4, 4]) == 3)
# print(what_is_different([4, 4, 4, 3]) == 3)

# data types

# lists numbers

# Algorithm
# itereate over the list of numbers, if one shows up only once return that number


# code

def what_is_different(numbers):
    for num in set(numbers):
        if numbers.count(num) == 1:
            return num

print(what_is_different([0, 1, 0]) == 1)
print(what_is_different([7, 7, 7, 7.7, 7]) == 7.7)
print(what_is_different([1, 1, 1, 1, 1, 1, 1, 11, 1, 1, 1, 1]) == 11)
print(what_is_different([3, 4, 4, 4]) == 3)
print(what_is_different([4, 4, 4, 3]) == 3)