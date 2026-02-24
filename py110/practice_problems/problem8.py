# create a function 

# input --> Non empty string
# output --> return the length of the longest vowel substring


# rules:
# the string consists entirely of lowercase alphabetic characters
# vowels are aeiou



# examples

# print(longest_vowel_substring('cwm') == 0)
# print(longest_vowel_substring('many') == 1)
# print(longest_vowel_substring('launchschoolstudents') == 2)
# print(longest_vowel_substring('eau') == 3)
# print(longest_vowel_substring('beauteous') == 3)
# print(longest_vowel_substring('sequoia') == 4)
# print(longest_vowel_substring('miaoued') == 5)

# data types

# input --> string
# output --> length of longest substring (integer)

# algorithm
# create a variable that stores a substring of vowels
# create another variable that stores length of the longest substring of vowels
# create a collection that includes all the vowels
# go through each character of the string. 
# If there is a vowel add it to the collection that stores the substring of vowels. 
# if the next one is a vowel than add it to teh collection
# if it is not, we reset the substring
# at some point we should be checking if the length of the substring is greater than the previous
# we then continue until the next vowel and we start the process again until we reach the end of the string
# return the length of the longest substring of vowels

def longest_vowel_substring(word):
    longest_length = 0
    current_count = 0
    vowels = 'aeiou'
    for char in word:
        if char in vowels:
            current_count += 1
        else:
            current_count = 0 
        if current_count > longest_length:
            longest_length = current_count
    return longest_length


print(longest_vowel_substring('cwm') == 0)
print(longest_vowel_substring('many') == 1)
print(longest_vowel_substring('launchschoolstudents') == 2)
print(longest_vowel_substring('eau') == 3)
print(longest_vowel_substring('beauteous') == 3)
print(longest_vowel_substring('sequoia') == 4)
print(longest_vowel_substring('miaoued') == 5)