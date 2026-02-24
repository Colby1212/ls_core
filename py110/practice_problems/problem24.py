# write a function that returns a list of all substrings of a string that are palindromic
# each substring must consist of the same sequence of characters forwards as backwards
# the substring in the returned list should be sorted by their appearance in the input string

# input --> string
# output --> list of palindromic substrings

# Rules --> The substrings must be at least 2 characters long
# currently unsure if it is case sensitive or not. The exmaples provided are all in lowercase

# can assume it is case sensitive unless otherwise specified
# unsure if we should include white spaces

# examples:
# print(palindromic_substrings("abcd") == [])
# print(palindromic_substrings("madam") == ["madam", "ada"])
# print(palindromic_substrings("hello-madam-did-madam-goodbye")
#       == ["ll", "-madam-", "-madam-did-madam-", "madam",
#           "madam-did-madam", "ada", "adam-did-mada", "dam-did-mad",
#           "am-did-ma", "m-did-m", "-did-", "did", "-madam-", "madam",
#           "ada", "oo"])
# print(palindromic_substrings("knitting cassettes")
#       == ["nittin", "itti", "tt", "ss", "settes", "ette", "tt"])


# data structures:
# strings and lists

# algorithm:
# iterate over each index of the string as a starting point 
# at each starting point we will check if the substrings from the starting point are palindromic

# if they are we will add them to a results list
# return the results list when we are done iterating


def palindromic_substrings(string):
    palindromes = []
    for starting_index in range(len(string)):
        for ending_index in range(starting_index + 1, len(string)):
            substring = string[starting_index: ending_index +1]
            if substring == substring[::-1]:
                palindromes.append(substring)
    print(palindromes)
    return palindromes



print(palindromic_substrings("abcd") == [])
print(palindromic_substrings("madam") == ["madam", "ada"])
print(palindromic_substrings("hello-madam-did-madam-goodbye")
      == ["ll", "-madam-", "-madam-did-madam-", "madam",
          "madam-did-madam", "ada", "adam-did-mada", "dam-did-mad",
          "am-did-ma", "m-did-m", "-did-", "did", "-madam-", "madam",
          "ada", "oo"])
print(palindromic_substrings("knitting cassettes")
      == ["nittin", "itti", "tt", "ss", "settes", "ette", "tt"])


def palidndromic_substrings(string):
    return [string[s:e] for s in range(len(string)) for e in range(s + 1, len(string))]