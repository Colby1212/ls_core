#Return a new list identical in structure, but with each number incremented by 1. 

lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

#def increment_values(dict_lst):
    #for item in dict_lst:
        #new_dict = {key: value + 1 for key, value in item.items()}
        #print(new_dict)


#increment_values(lst)

new_lst = [{key: value + 1 for key, value in item.items()} for item in lst]

print(new_lst)