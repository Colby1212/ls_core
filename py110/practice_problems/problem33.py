# write a function that takes two sorted lists as arguments
# return a new list that contains the elements from both input lists in sorted order

# input --> 2 sorted lists
# output --> one sorted list of both elements in ascending order


# Rules:
# Currently it looks like all items of the list are integers
# cannot use the sort() method or sorted() method

# Examples and Test cases

# Test Cases:
# print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
# print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
# print(merge([], [1, 4, 5]) == [1, 4, 5])
# print(merge([1, 4, 5], []) == [1, 4, 5])


# If the list a list is empty than the non empty list is returned

# Data types
# Integers, lists, Greater than less than? comparing operators?

# Algorithm
# Create an empty list
# Iterate over one list
# Compare the item to each item in the other list
# the one that is less than the other is removed, we then repeat for each item in the first list until one list is empty
# if one list is empty we add the remaining elements of the non=emty list to the list we created
# return the new sorted list of items


def merge(list1, list2):                     
    ordered_list = []
    copy1 = list1[::]
    copy2 = list2[::]
    while True:
        if copy1 == []:
            ordered_list.extend(copy2)
            return ordered_list
        if copy2 == []:
            ordered_list.extend(copy1)
            return ordered_list
        if copy1[0] <= copy2[0]:
            ordered_list.append(copy1.pop(0))
        if copy2[0] < copy1[0]:
            ordered_list.append(copy2.pop(0))
        print(ordered_list)

print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])


def merge(list1, list2):
   ordered = []
   i = 0
   j = 0
   while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            ordered.append(list1[i])
            i += 1
        else:
            ordered.append(list2[j])
            j += 1
   ordered.extend(list1[i:])
   ordered.extend(list2[j:])
   return ordered

print(merge([1, 5, 9], [2, 6, 8]) == [1, 2, 5, 6, 8, 9])
print(merge([1, 1, 3], [2, 2]) == [1, 1, 2, 2, 3])
print(merge([], [1, 4, 5]) == [1, 4, 5])
print(merge([1, 4, 5], []) == [1, 4, 5])