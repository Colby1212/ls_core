# write a function that takes a dictionary of file names and owner namesit returns a new dictionary where the keys are the owner names
# and the values are lists of their fule names

# files = {
#     'Input.txt': 'Randy',
#     'Code.py': 'Stan',
#     'Output.txt': 'Randy'
# }

# expected_output = {
#     'Randy': ['Input.txt', 'Output.txt'],
#     'Stan': ['Code.py']
# }

# print(group_by_owners(files) == expected_output)

# input --> a dictionary of file names and owner names
# output -->  a new dictionary where the keys are the owner names, and values are lists of their file names

# In the example above we see that randy owns two files, input.txt and output.txt
# so the new output has {'randy': [output.txt, input.txt]}

# Data types:
# dictionaries, strings, lists


# Algorithm:
# create a new dictionary
# find all unique names in the values of the original dictionary
# for each name, find all the files that belong to that name
# add each file to a list and assign that list to the name in the new dictionary
# return the new dictionary

def group_by_owners(files):
    result = {}
    for owner in set(files.values()):
        result[owner] = [file for file, file_owner in files.items() if file_owner ==owner]
    return result

files = {
    'Input.txt': 'Randy',
    'Code.py': 'Stan',
    'Output.txt': 'Randy'
}

expected_output = {
    'Randy': ['Input.txt', 'Output.txt'],
    'Stan': ['Code.py']
}

print(group_by_owners(files) == expected_output)