# create a function that takes a list of integers as an argument
# and returns a tuple of two numbers that are closest together in value
# if there are multiple pairs that are equally close, return the pair that occurs first

# input --> List of integers
# output --> Tuple of the two integers within the list that are closest 


# print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
# print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
# print(closest_numbers([12, 22, 7, 17]) == (12, 7))

# algorithm

# 1. create a function that takes a list of inteers as an argument
# 2. Find the difference between each of the numbers
# 3. Return the a tuple ((num1, num1)) two numbers in the list with the smallest difference
# 4. if there is a tie than we return the first one that appears in the list
# 1. iterate over the numbers, starting at index 1, then compare the difference between the rest of the numbers
# 2. as we iterate we keeping record of the lowest difference. When we find one replace the tuple with the current two numbers
# 3. have a tuple in place before the iteration, start the difference at the first two digits. 
# 4. after comparing the numbers to the first index we move onto the next. Note that we only need to compare the starting number with the ones that come after iterate
# 5. return the tuple with the two numbers

def closest_numbers(nums):
    current_lowest = abs(nums[0] - nums[1])
    num1, num2 = nums[0], nums[1]
    for idx in range(len(nums) -1):
        for char in nums[idx+1:]:
            if abs(nums[idx] - char) < current_lowest:
                current_lowest = abs(nums[idx] - char)
                num1, num2 = nums[idx], char
    print(num1, num2)
    return (num1, num2)

print(closest_numbers([5, 25, 15, 11, 20]) == (15, 11))
print(closest_numbers([19, 25, 32, 4, 27, 16]) == (25, 27))
print(closest_numbers([12, 22, 7, 17]) == (12, 7))