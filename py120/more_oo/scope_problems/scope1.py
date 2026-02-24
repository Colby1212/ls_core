'''
Write a program that asks the user for two numbers and
divides the first by the second. Handle any potential ZeroDivisionError or ValueError exceptions(There is no need to retry inputs in this problem)
'''

try:

    num1 = float(input('Enter the first number: '))
    num2 = flat(input('Enter the second number: '))

    result = num1 / num2
    print('The result is: {result}')

except ZeroDivisionError:
    print('Cannot divide by zero!')

except ValueError
    print('Please enter valid numbers!')
