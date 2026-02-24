'''

Given the following list:
numbers = [1, 2, 3, 4, 5]

Write two functions to fetch the sicth element from the list: one using the LBYL approach 
and another using the AFNP approach. In both cases, the function should return None when the element isn't found

'''


def get_sixth_afnp(numbers):
    try:
        return numbers[5]
    except IndexError:
        return None

def get_sixth_lbyl(numbers):
    if len(numbers) > 5:
        return numbers[5]

    return numbers[5]