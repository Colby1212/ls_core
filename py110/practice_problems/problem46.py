# write a function that displays a four pointed diamond in a nxn grid

# where n is an odd Integersyou may assume that the argument will always be an odd integer



# Input  --> integer
# output --> a nxn grid that displays a star

# examples and test cases 

# Test Cases:
# diamond(1)
# # Expected Output:
# # *

# diamond(3)
# # Expected Output:
# #  *
# # ***
# #  *

# diamond(9)
# # Expected Output:
# #     *
# #    ***
# #   *****
# #  *******
# # *********
# #  *******
# #   *****
# #    ***
# #     *


# data types
# strings, integer


# algorithm
# create a 9x9 grid
# A diamon is made up of *
# The first line should contain 1 *
# increase the amount of *'s by 2 fir ech line until we reach n *'s
# When we reach n *s the next lines should have 2 less than the previous
# repeat until we have 1 * in the last line

# code 

def diamond(num):
    lines = []
    for multiplier in range(1,num +1, 2):
        lines.append( '*' * multiplier)
    lines.extend(lines[-2::-1])
    for line in lines:
        print(line.center(n))

diamond(9)