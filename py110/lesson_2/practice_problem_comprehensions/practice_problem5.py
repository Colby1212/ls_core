#Sort the list so that the sub-lists are ordered based on the sum of the odd numbers that they contain. Dont mutate the original
#Try to use a comprehension in your solution

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

def add_odd_numbers(sublist):
    sum = 0
    for num in sublist:
        if num % 2 == 1:
            sum += num
    return sum

def add_odd_numbers2(sublist):
    odd_numbers = [num for num in sublist if num % 2 != 0]
    return sum(odd_numbers)

new_lst1 = sorted(lst, key = add_odd_numbers)
new_lst2 = sorted(lst, key = add_odd_numbers2)

print(new_lst1)
print(new_lst2)