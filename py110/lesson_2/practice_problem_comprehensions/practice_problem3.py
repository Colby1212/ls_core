#Return a new list with the same structure, but with the values in each sublist ordered
#in ascending order as strings. Use comprehension if you can. Try using a for loop first. 

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]


sorted_lst = []
for sublist in lst:
    sorted_lst.append(sorted(sublist, key = str))

sorted_lst2 = [sorted(sublist, key = str) for sublist in lst]

print(lst)
print(sorted_lst)
print(sorted_lst2)