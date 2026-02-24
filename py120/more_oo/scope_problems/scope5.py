'''
Modify Your answer from the previous problem and raise a custom exception NegativeNumberError instead of an ordinary ValueERrror exception

'''


num1 = float(input('Please input a number: '))

if num < 0:
    raise NegativeNumberError('Negative numbers are not allowed!')

print(f'You entered {num}')