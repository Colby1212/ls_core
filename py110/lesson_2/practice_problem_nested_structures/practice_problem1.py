#demonstrate how you would access the letter 'g' in each structure below

lst = ['a', 'b', ['c',['d', 'e', 'f', 'g']]]

print(lst[2][1][3])

lst2 = [
    {
        'first': ['a', 'b', 'c'],
        'second': ['d', 'e', 'f']
    },
    {
        'third': ['g', 'h', 'i']
    }
]

print(lst2[1]['third'][0])

lst3 = [['abc'], ['def'], {'third': ['ghi']}]

print(lst3[2]['third'][0][0])

dict1 = {'a': ['d', 'e'], 'b': ['f', 'g'], 'c': ['h', 'i']}

print(dict1['b'][1])

dict2 = {'1st': {'d': 3}, '2nd': {'e': 2, "f": 2}, '3rd': {'g': 0}}

print(dict2['3rd'])
