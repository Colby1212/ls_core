create a function that takes two string arguments and returns the number of times
that the second string occurs in the first
Note that overlapping strings dont count. 

input --> two strings 
output --> integer --> # of times string 2 is found in string 1. no overlaps


examples

print(count_substrings('babab', 'bab') == 1)
print(count_substrings('babab', 'ba') == 2)
print(count_substrings('babab', 'b') == 3)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('babab', 'x') == 0)
print(count_substrings('', 'x') == 0)
print(count_substrings('bbbaabbbbaab', 'baab') == 2)
print(count_substrings('bbbaabbbbaab', 'bbaab') == 2)
print(count_substrings('bbbaabbbbaabb', 'bbbaabb') == 1)

def count_substrings(string1, string2):
    return string1.count(string2)