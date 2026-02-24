# you have 1000 klugts tgat are initially off. You make 1000 passes over the lights

# On the first pass you toggle every light 
# on the second pass you toggle every 2nd light
# on the third pass, you toggle every 3rd light
# and so on up to the 1000th passWrite a function that takes the total number of lightsn as an argument and returns a list of the lights that are on after n passes


# input --> Integers
# output --> a list of lights that are on?

# Examples / test cases

# print(lights_on(5) == [1, 4])
# print(lights_on(100) == [1, 4, 9, 16, 25, 36, 49, 64, 81, 100])



# lets look at 5

# so they are all off
# 0 = off, 1 = on
# before first pass --> 0, 0, 0, 0, 0
# first pass --> 1, 1, 1, 1, 1
# second pass 1, 0, 1, 0, 1
# third pass 1, 0, 0, 0, 1
# fourth pass 1, 0, 0, 1, 1
# fifth pass 1, 0, 0, 1, 0
# odd  = on
# even = off


# Data types 

# collection, lists, nums, ranges

# algorithm
# create a dictionary of how many times each number is passed over (or toggled)
# loop over the list n times, the nth iteration is how many steps it takes
# 1 = 1, 2 = 2, 3 = 3, etc. 
# At each iteration track which numbers were went over. 
# after the n iterations check which numbers were toggled an even amount of times 
# add the numbers at which they were toggled an odd number of times to a list, return the list 



# Code:


def lights_on(number):
    toggle_count = {}
    for step in range(1, n + 1):
        for light in range(step, n +1, step):
            toggle_count[light] = toggle_count.get(light, 0) + 1
    return [light for light, count in toggle_count.items() if count % 2 != 0]

print(lights_on(5) == [1, 4])



def lights_on(n):
    return [i * i for i in range(1, int(n ** 0.5) + 1)]