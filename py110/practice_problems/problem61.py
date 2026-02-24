# Create a function that takes a nonempty string as an argument
# return a tuple consisting of a string an dna integer
# if we call the string argument s, the string component of the returned tuple t, and the integer component last
# then s, t, k must be related so that s == t * k
# The values of 2 and k should be the shorted possible substring and the largest possible repeat count 


# input --> string
# output --> tuple of a string and integer

# Rules 
# The values of t and k should be the shortes possible substring and largest possible repeat count

# Examples and test cases 

# print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
# print(repeated_substring('xyxy') == ('xy', 2))
# print(repeated_substring('xyz') == ('xyz', 1))
# print(repeated_substring('aaaaaaaa') == ('a', 8))
# print(repeated_substring('superduper') == ('superduper', 1))


# No overlaps

# Data types

# tuples, int, string


# Algorithm

# Interate over each substring in the first half of the string
# if the you repeat the substring n amount of times and it becomes the original string than return the substring and new
# repeat until you iterate over a substirng that is half of the original string in length
# if you finish this wihtout returning anything return the original string and 1



# code

def repeated_substring(string):
    mid_point = (len(string) // 2) + 1

    for index in range(mid_point):
        substring = string[:index]
        print(substring)
        count = string.count(substring)
        if substring * count == string:
            return (substring, count)
    
    return (string, 1)

print(repeated_substring('xyzxyzxyz') == ('xyz', 3))
print(repeated_substring('xyxy') == ('xy', 2))
print(repeated_substring('xyz') == ('xyz', 1))
print(repeated_substring('aaaaaaaa') == ('a', 8))
print(repeated_substring('superduper') == ('superduper', 1))