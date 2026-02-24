#Write some code to return a list that contains only the dictionaries where all the numbers are even. 


lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]



def all_even_numbers(dict_item):
    for value in dict_item.values():
        for num in value:
            if num % 2 != 0:
                return False
    return True

new_lst = [{key: value for key, value in item.items()} for item in lst if all_even_numbers(item)]

print(new_lst)