def sort_by_consonant_count(strings):
    strings.sort(key=count_max_adjacent_consonants, reverse=True)
    return strings



def count_max_adjacent_consonants(string):
    string = ''.join(string.split(' '))
    max_consonant_count = 0
    adjacent_consonants = ''

    for letter in string:
        if letter.lower() in 'bcdfghjklmnpqrstvxyz':
            adjacent_consonants += letter
            if len(adjacent_consonants) > max_consonant_count: 
                if len(adjacent_consonants)> 1:
                    max_consonant_count = len(adjacent_consonants)

        else:
            if len(adjacent_consonants) > max_consonant_count:
                if len(adjacent_condonants) > 1:
                    max_consonant_count = len(adjacent_consonants)

            adjacent_consonants = ''
        
    return max_consonant_count

my_list = ['asdsad', 'asdsadas', 'asdddsdsd', 'wwwewwewewww', 'wuuuuur']

print(sort_by_consonant_count(my_list))