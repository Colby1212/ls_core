# create a function that takes a list of integers as an argument
# and returns the integer that appears an odd number of times
# There will always be exactly one integer in the input list


# input --> list of integers
# output --> integer that has appeared an odd number of times

# Rules --> there will always be one integer in the input list


# Examples 

# print(odd_fellow([4]) == 4)
# print(odd_fellow([7, 99, 7, 51, 99]) == 51)
# print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
# print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
# print(odd_fellow([0, 0, 0]) == 0)



# Data types 

# Lists, collection, integer


# Algorithm

# Create a dictionary to track the amount of times an integer is in the list
# iterate through the list of numbers
# Go through dictionary and find the integer that is not divisible by two
# Return that integer



def odd_fellow(numbers):
    track_nums = {}
    for num in numbers:
        track_nums[num] = track_nums.get(num, 0) + 1
    for num in track_nums:
        if track_nums[num] % 2 != 0:
            return num

print(odd_fellow([4]) == 4)
print(odd_fellow([7, 99, 7, 51, 99]) == 51)
print(odd_fellow([7, 99, 7, 51, 99, 7, 51]) == 7)
print(odd_fellow([25, 10, -6, 10, 25, 10, -6, 10, -6]) == -6)
print(odd_fellow([0, 0, 0]) == 0)
