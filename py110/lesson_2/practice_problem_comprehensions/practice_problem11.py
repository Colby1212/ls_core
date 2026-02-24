#Write some code to create a list of every vowel that appears in the contained strings, then print it. 

#Start by trying to write this using nested loops

#Once your nested loop code works, try to refactor the code so it uses sinlge list comprehension 
#You can print the resulting list outside of the comprehension. 

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

vowels = 'AEIOUaeiou'
list_of_vowels = []

list_of_vowels2 = [char for element in dict1.values() 
                        for word in element 
                        for char in word if char in vowels]


list_of_vowels3 = [char for key in dict1
                        for word in dict1[key]
                        for char in word if char in vowels]

for lists in dict1.values():
    for element in lists:
        for char in element:
            if char in vowels:
                list_of_vowels.append(char)
print(list_of_vowels)
print(list_of_vowels2)
print(list_of_vowels3)

