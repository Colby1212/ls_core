#write code that uses comprehensions to define a dictionary where the key is the first item in each sublist, and the value is the second

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

new_dict = {item[0]: item[1] for item in lst}

print(new_dict)