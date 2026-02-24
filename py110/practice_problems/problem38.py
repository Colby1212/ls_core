# Write a function that computes the scrabble score for a given word:

# The function should take a string as an argument and return the total score


# The letter values are as follows:
# | Letters                      | Value |
# | ---------------------------- | :---: |
# | A, E, I, O, U, L, N, R, S, T |   1   |
# | D, G                         |   2   |
# | B, C, M, P                   |   3   |
# | F, H, V, W, Y                |   4   |
# | K                            |   5   |
# | J, X                         |   8   |
# | Q, Z                         |   10  |



# input --> string
# output --> integer (sum of the value of each letter according to scrabble rules)


# Examples / test cases 

# print(scrabble_score('cabbage') == 14)
# print(scrabble_score('CABBAGE') == 14)
# print(scrabble_score('hello') == 8)
# print(scrabble_score('quiz') == 22)
# print(scrabble_score('') == 0)



# empty strings still return a score
# This is not case sensitive


# Data types

# Integers, strings


# Algorithm

# Allocate a value to each letter according to teh table above
# Because it is case insensitive, make all letters lowercase
# Iterate through the word and check the value of each character
# sum the values
# return the total sum


# Code:

def letter_value(letter):
    match letter:
        case 'A'|'E'|'I'|'O'|'U'| 'L'| 'N'| 'R'| 'S'| 'T':
            return 1
        case 'D'| 'G':
            return 2
        case 'B'| 'C'| 'M'| 'P':
            return 3
        case 'F'| 'H'|'V' |'W' |'Y':
            return 4
        case 'K':
            return 5
        case 'J'| 'X':
            return 8
        case 'Q'| 'Z':
            return 10
        case_:
            return 0

def scrabble_score(word):
    score = 0 
    for char in word.upper():
        score += letter_value(char)
    return score

print(scrabble_score('cabbage') == 14)
print(scrabble_score('CABBAGE') == 14)
print(scrabble_score('hello') == 8)
print(scrabble_score('quiz') == 22)
print(scrabble_score('') == 0)