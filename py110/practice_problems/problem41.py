# Write a function that takes a list of numbers
# and sorts it using the merge sort algorithm
# (divides the list until each list only contains one item)
# then it merges it back together while sorting it.

# input --> a list of a singular type
# output --> a new sorted list

# Rules --> Need to use the merge sort algorithm
# A recursive function that breaks the list down and then sorts it while putting it back together


# Examples / test cases 

# Test Cases:
# print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
# print(merge_sort([5, 3]) == [3, 5])
# print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
# print(merge_sort([
#     'Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie'
# ]) == ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'])
# print(merge_sort([
#     7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46
# ]) == [
#     1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54
# ])


# we dont see it but it should be a recursive function that sorts the items in ascending order


# data types

# Integers, collections, recursive function


# algorithm

# 1. Break the list in half
# 2. repeat until each list only contains a singular element
# 3. combine two lists together and sort the list while doing sort
# 4. repeat until it is a singular sorted list


# code
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid_point = (len(lst) // 2)
    left = lst[:mid_point]
    right = lst[mid_point:]

    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)

def merge(list1, list2):
    copy_list1 = list1[::]
    copy_list2 = list2[::]
    result = []

    while copy_list1 and copy_list2:
        if copy_list1[0] < copy_list2[0]:
            result.append(copy_list1.pop(0))
        else:
            result.append(copy_list2.pop(0))
    return result + copy_list1 + copy_list2


print(merge_sort([9, 5, 7, 1]) == [1, 5, 7, 9])
print(merge_sort([5, 3]) == [3, 5])
print(merge_sort([6, 2, 7, 1, 4]) == [1, 2, 4, 6, 7])
print(merge_sort([
    'Sue', 'Pete', 'Alice', 'Tyler', 'Rachel', 'Kim', 'Bonnie'
]) == ['Alice', 'Bonnie', 'Kim', 'Pete', 'Rachel', 'Sue', 'Tyler'])
print(merge_sort([
    7, 3, 9, 15, 23, 1, 6, 51, 22, 37, 54, 43, 5, 25, 35, 18, 46
]) == [
    1, 3, 5, 6, 7, 9, 15, 18, 22, 23, 25, 35, 37, 43, 46, 51, 54
])