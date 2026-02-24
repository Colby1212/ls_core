'''
Expand your answer to the previous program so it print the result only when no exceptions are raised
You should also print end of the program regardless of whether an exception is raised
'''

try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2
except ZeroDivisionError:
    print("Cannot divide by zero!")

except ValueError:
    print('Please input valid numbers')

else:
    print(f'The result is {result}')

finally:
    print('End of Program!')