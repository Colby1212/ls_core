# create a function that takes a string argument
# it willl return a copy of the string with every second character in every third word converted to uppercase
# Other characters should remain the same

# Input --> String argument
# output --> Copy of the string with every second character in every third word converted to uppercase

# original = 'Lorem Ipsum is simply dummy text of the printing world'
# expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
# print(to_weird_case(original) == expected)

# original = 'It is a long established fact that a reader will be distracted'
# expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
# print(to_weird_case(original) == expected)

# print(to_weird_case('aaA bB c') == 'aaA bB c')

# original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
# expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
# print(to_weird_case(original) == expected)


# Looking at the test cases, we can see that it is at every index 2, 5, 8,....
# and every other word 1,3,5, 



# Algorithm 
# Iterate over the individual words in the string
# IF the word is at indexes 2, 5, 8... than every other character in that string (idexes 1, 3, 5) is converted to uppercase
# IF the word is not in those indexes than it remains the same
# Split the string into individual words.
# Split the individual words into indivdual characters, replace every other character with an uppercased character, 
# if there is only a singular character, leave the word alone


def to_weird_case(original):
    words = original.split()
    special_indices = range(2, len(words), 3)
    # for idx in range(2,len(word_list) + 1, 3):
    #     word_list[idx] = capatalize_every_other(word_list[idx])
    # return ' '.join(word_list)
    return ' '.join([capatalize_every_other(words[i]) if i in special_indicies 
                    else word[i] for i in range(len(words))])

def capatalize_every_other(word):
    return ''.join([char.upper() if value % 2 != 0 else char for value, char in enumerate(word)])

original = 'Lorem Ipsum is simply dummy text of the printing world'
expected = 'Lorem Ipsum iS simply dummy tExT of the pRiNtInG world'
print(to_weird_case(original) == expected)

original = 'It is a long established fact that a reader will be distracted'
expected = 'It is a long established fAcT that a rEaDeR will be dIsTrAcTeD'
print(to_weird_case(original) == expected)

print(to_weird_case('aaA bB c') == 'aaA bB c')

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
