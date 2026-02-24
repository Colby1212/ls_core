#a UUID (universally unique identifier) is a type of identifier often used to uniquely identify items, even when some of those items were created
#on a different server or by a different application. That is, without any sychronization, two or more computer systems
#can create new items and label them with a uUUID, with no significant risk of stepping on each other's toes. 
# It accomplishes this feat through massive randomization. The number of possible UUID values is approx 3.4 x 10E^38. 
#The chance of a conflict, a colision is vanishingly small with such large numer of possible values. 

#Each UUID consists of 32 hexadecimal characters (the digits 0-9, and the letters a-f) represented as a string. 
#The value is typically broken into 5 sections in an 8-4-4-4-12 pattern. 

#Write a function tha takes no arguments and returns a strng that contains a UUID

#PEDAC

#P --> Understand the Problem
#input: no input
#output a string that contains a UUID
#rules:
    #generate a UUID
    #32 hexadecimal characters (digits 0-9, and letters a-f)
    #all lowercase
    #broken into 5 sections in an 8-4-4-4-12 pattern

#E --> Examples/Test Cases
#generate_UUID() --> 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'

#D --> Data Structure
#string

#A --> Algorithm
#1. 5 sections = [8, 4, 4, 4, 12]
#2. create a string of 32 first or create 5 sections and join them
#3. Each character in each section is a random hexadecimal character
#4. Makes more sense to create 5 sections and join them. 

#C --> Code

#import random
# def generate_UUID():
# sections = [8, 4, 4, 4, 12]
# use range to determine how many characters to generate for each section. 

import random

def generate_UUID():
    sections = [8, 4, 4, 4, 12]
    hexadecimal_chars = '0123456789abcdef'
    uuid = []
    
    for number in sections:
        string_selection = [random.choice(hexadecimal_chars) for char in range(number)]
        uuid.append(''.join(string_selection))

    return '-'.join(uuid)

print(generate_UUID())


