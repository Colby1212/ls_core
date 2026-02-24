#Compute and display the total age of the family's male members. Try working out the answer two ways:
#1. WIth an rodinary loop
#2. With a comprehension 

munsters = {
    'Herman': {'age': 32, 'gender': 'male'},
    'Lily': {'age':30, 'gender': 'female'},
    'Grandpa': {'age': 402, 'gender': 'male'},
    'Eddie': {'age': 10, 'gender': "male"},
    'Marilyn': {'age': 23, 'gender': 'female'},
}


sum_age_munsters = []

for munster in munsters.keys():
    if munsters[munster]['gender'] == 'male':
        sum_age_munsters.append(munsters[munster]['age'])
    
print(sum(sum_age_munsters))


sum_age_munsters2 = sum([munsters[munster]['age'] for munster in munsters if munsters[munster]['gender'] == 'male'])

print(sum_age_munsters2)