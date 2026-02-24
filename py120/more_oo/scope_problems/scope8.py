'''

Write a python functon get_age(name) that takes a student's name as an argument and returns their age.
If the Student's name isnt in the dictionary, the function should return 'Student not found'

'''

def get_age(name):
    try:
        return students[name]
    except KeyError:
        return 'Student not found'