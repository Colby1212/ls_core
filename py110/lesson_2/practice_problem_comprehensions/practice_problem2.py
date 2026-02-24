#Given the following data structure, return a new list with the same structure
#but with the valies in each sublist ordered in ascending order
#Use a comprehension. Try using a for loop first

lst = [['b', 'c', 'a'], [2, 11, -3], ['blue', 'black', 'green']]

#expected result --> [['a', 'b', 'c'], [-3, 2, 11], ['black', 'blue', 'green']]\

sorted_lst = []
for sublist in lst:
    sorted_lst.append(sorted(sublist))


sorted_lst2 = [sorted(sublist) for sublist in lst]

print(lst)
print(sorted_lst2)
print(sorted_lst)