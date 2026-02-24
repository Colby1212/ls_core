# write a function 
# that takes a list of lists and returns a one dimensional list
# In each one of the nested lists, the first element is the fruit and the second is the quantity
# The one dimensional list should contain each fruit as many times as the quantity

# Examples

# groceries = [['apple', 3], ['orange', 1], ['banana', 2]]
# # result: ['apple', 'apple', 'apple', 'orange', 'banana', 'banana']
# print(buy_fruit(groceries) == ['apple', 'apple', 'apple', 'orange', 'banana', 'banana'])

# apple, 3 --> apple, apple, apple
# orange, 1 --> orange

# Data types
# Lists, strings, integers, nested lists


# Algorithm
# Iterate through each item in the grocery list
# For each item get the fruit and the quantity
# the new list should include the fruit as many times as the quantity
# repeat this for each sublist in the grocery list


# Code

def buy_fruit(grocery_list):
    result = []
    for item in grocery_list:
        fruit = item[0]
        quantity = item[1]
        result.extend([fruit] * quantity)
    return result

groceries = [['apple', 3], ['orange', 1], ['banana', 2]]
# result: ['apple', 'apple', 'apple', 'orange', 'banana', 'banana']
print(buy_fruit(groceries) == ['apple', 'apple', 'apple', 'orange', 'banana', 'banana'])

def buy_fruit(grocery_list):
    return [fruit for fruit, quantity in grocery_list for _ in range(quantity)]

groceries = [['apple', 3], ['orange', 1], ['banana', 2]]
# result: ['apple', 'apple', 'apple', 'orange', 'banana', 'banana']
print(buy_fruit(groceries) == ['apple', 'apple', 'apple', 'orange', 'banana', 'banana'])