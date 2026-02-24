# create a function that takes a string argument

# and returns a copy of the string with every second character in every third word converted to uppercase

# Other characters should remian the smaller

# input --> string
# output --> modified copy of the string


# Rules

# every third word --> indexes 2, 5, 8, etc. 
# Every other word --> indexes, 1, 3, 5

# Examples and test cases 

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

# Algorithm

# Itereate over every third word of the string
# In each of the words, every other letter is capatalized 
# return a new copy of the string


# code:


def capatalize_every_other(word):
    return ''.join([char.upper() if index % 2 ==1 else char for index, char in enumerate(word) ])

def to_weird_case(string):
    words = string.split()
    for idx in range(2, len(words), 3):
        words[idx] = capatalize_every_other(words[idx])
    return ' '.join(words)

original = "Mary Poppins' favorite word is supercalifragilisticexpialidocious"
expected = "Mary Poppins' fAvOrItE word is sUpErCaLiFrAgIlIsTiCeXpIaLiDoCiOuS"
print(to_weird_case(original) == expected)
