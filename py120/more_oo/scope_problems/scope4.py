'''
Write a program that asks the user for a number
IF the input isnt a number, let python raise an appropriate exception
If the number is negative, raise ValueError with an appropriate error message
If the number isnt negative, print a message that shows its value
'''


num1 = float(input('Please input a number: '))

if num < 0:
    raise ValueError('Negative numbers are not allowed!')

print(f'You entered {num}')