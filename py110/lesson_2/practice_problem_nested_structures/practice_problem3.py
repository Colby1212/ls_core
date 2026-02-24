#Given the following code, what will the final values of a and b be? Try to answer without running the code.

a = 2
b = [5, 8]

lst = [a, b]

lst[0] += 2

lst[1][0] -= a

print(lst)

#lst = [2, [5,8]]
#lst[0] += 2 --> lst = [4, [5, 8]]
#lst[1][0] -= a --> lst = [4, [3, 8]]
#The final value of the list will be [4, [3, 8]]