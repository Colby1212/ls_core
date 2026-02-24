'''
Modify your answer to the previous problem so it handles both ZeroDivisionError and ValueError with a single exception handler.
The output for oth exception types can be obtained from the exception object

'''


try:
    num1 = float(input('Enter the first number: '))
    num2 = float(input('Enter the second number: '))
    result = num1 / num2

except (ZeroDivisionError, ValueError) as e:
    print(e)

else:
    print(f'The result is: {result}')

finally:
    print('End of the program')