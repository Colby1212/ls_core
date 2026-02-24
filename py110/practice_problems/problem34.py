# a featured number is an odd number that is a multiple of 7, with all of its difits occuring once
# Write a function that takes an integer as an argument 
# and returns teh next featured number greater than the argument
# Issue an error message if there is no next featured number. 

# Input --> Integer
# Output --> Featured number (odd multiple of 7 that only has each digit occuring once)
# Largest featured number --> 9876543201

# Examples/data types

# print(featured(12) == 21)
# print(featured(20) == 21)
# print(featured(21) == 35)
# print(featured(997) == 1029)
# print(featured(1029) == 1043)
# print(featured(999999) == 1023547)
# print(featured(999999987) == 1023456987)
# print(featured(9876543200) == 9876543201)
# print(featured(9876543201) == "There is no possible number that fulfills those requirements.")


# If its already a featured number we need the NEXT one
# The largest possible featured number is 9876543201

# Data types
# Integers

# Algorithm
# Take the integer inputed, and add one
# Check to see if the number is a multiple of 7. 
# If it is not a multiple of 7, make it a multiple of 7
# Check to see if the integer is even or odd, if it is even, add 7 to the number
# Now check if it is a featured number
# add 14 to the number until it is a featured number
# return the number

# Code

def featured(num):
    num = num + 1
    if num % 7 != 0:
        num = num + (7 - (num%7))
    if num % 2 ==0:
        num = num + 7
    while True:
        if num > 9876543201:
            return "There is no possible number that fulfills those requirements."
        if is_featured(num):
            return num
        else:
            num += 14

def is_featured(num):
    count = {}
    for number in str(num):
        count[number] = count.get(number, 0) + 1
    for nums in count.values():
        if nums != 1:
            return False
    return True


print(featured(12) == 21)
print(featured(20) == 21)
print(featured(21) == 35)
print(featured(997) == 1029)
print(featured(1029) == 1043)
print(featured(999999) == 1023547)
print(featured(999999987) == 1023456987)
print(featured(9876543200) == 9876543201)
print(featured(9876543201) == "There is no possible number that fulfills those requirements.")