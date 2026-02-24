#Given the object shown below, print the nanme, age, and gender of each family member.

munsters = {
    'Herman': {'age': 32, 'gender': 'male'},
    'Lily': {'age': 30, 'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie': {'age': 10, 'gender': 'male'},
    'Marilyn': {'age': 23, 'gender': 'female'}
}

for name in munsters.keys():
    print(f"{name} is a {munsters[name]['age']}-year-old {munsters[name]['gender']}.")

#Each output line should follow this pattern:
#(name) is a (age)-year-old (male or female). 