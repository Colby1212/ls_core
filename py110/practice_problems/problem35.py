# write a function that displays an 8 pointed star in an nxn grid
# where n is an odd integer that is supplied as an argument to the function 
# The smallest such star you need to handle is a 7x7 grid

# input --> Integer
# output --> 8 point star

# Rules? the integer will always be odd, 
# The smalled gri I will need to handle is a 7x7

# Examples/ data types

# Test Cases:
# star(7)
# # Expected output:
# # *  *  *
# #  * * *
# #   ***
# # *******
# #   ***
# #  * * *
# # *  *  *


# star(9)
# # Expected output:
# # *   *   *
# #  *  *  *
# #   * * *
# #    ***
# # *********
# #    ***
# #   * * *
# #  *  *  *
# # *   *   *


# ***
# Data types
# Integers, Strings

# Algorithm
# Create a input x input grid
# Each line row should have 3 '*' with spaces in between
# The amount of spaces in between the first row is (input - 3) /2 
# the next will have one less but leading and trailing white spaces
# when there are no spaces between the *'s than the next row contains * x input
# Now we increment the white spaces between the stars
# (Do the steps 2, 3, 4 in reverse)


# Code:
def star_row(lead, sep):
    return ' ' * lead + '*' + ' ' * sep + '*' + ' ' * sep+ '*'

def star(num):
    star_lines = []
    lead = 0
    sep = int((num - 3)/2)
    while sep >= 0:
        star_lines.append(star_row(lead, sep))
        lead += 1
        sep -=1 
    star_lines.append('*' * num)
    star_lines.extend(reversed(star_lines[0:-1]))
    for line in star_lines:
        print(line)

star(9)