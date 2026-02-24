# writw a function that takes a string and returns a dictionary containing the followign three

# 1. The percentage of characers that are lowercase
# 2. The percentage of characters that are uppercase
# 3. The percentage of characters that are neither

# you may assume that the string will always contain at least one character. The percentages should be represented as strings. 



# Test Cases:
# print(letter_percentages('abCdef 123') == {
#     'lowercase': "50.00",
#     'uppercase': "10.00",
#     'neither': "40.00",
# })
# 10 characters --> 5 lowercase, 1 uppercase, 4 neither. White spaces are included, rounded to two decimal places, and are strings
# print(letter_percentages('AbCd +Ef') == {
#     'lowercase': "37.50",
#     'uppercase': "37.50",
#     'neither': "25.00",
# })
# print(letter_percentages('123') == {
#     'lowercase': "0.00",
#     'uppercase': "0.00",
#     'neither': "100.00",
# })


# data types:
# dictionaries, strings, floats, integers


# Algorithm:
# create a new dictionary with the keys, lowercase, uppercase, neither
# count the number of lowercase characters in the string
# count the number of uppercase characters in the string
# count the number characters that are neither
# calculate the percentage of each category, format to two decimal places, and conver to a string

def letter_percentages(string):
    total_chars = len(string)
    lowercase_count = 0
    uppercase_count = 0
    neither_count = 0 
    for char in string:
        if char.islower():
            lowercase_count += 1
        elif char.isupper():
            uppercase_count += 1
        else:
            neither_count += 1
    result = {
        'lowercase': f"{lowercase_count / total_chars * 100:.2f}",
        'uppercase': f"{uppercase_count / total_chars * 100:.2f}",
        'neither': f"{neither_count / total_chars * 100:.2f}",
    }
    return result


print(letter_percentages('abCdef 123') == {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
})

print(letter_percentages('AbCd +Ef') == {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
})
print(letter_percentages('123') == {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
})
