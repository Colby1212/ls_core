#Write some code to return a list that contains the colours of the fruits and the sizes of the vegetables. 
#The sizes should be uppercase, and the colours should be capitalized. 

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}


def transform_item(item):
    if item['type'] == 'fruit':
        return[color.capitalize() for color in item['colors']]

    elif item['type'] == 'vegetable':
        return item['size'].upper()

result = [transform_item(item) for item in dict1.values()]
print(result)
