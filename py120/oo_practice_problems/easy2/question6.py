'''

Consider the following code:

class Cat:
    def __init__(self, type):
        self.type = type

print(Cat('Hairball'))

Update the code to produce the followng output:
'I am a hairball'

'''

class Cat:
    def __init__(self, type):
        self.type = type
    
    def __str__(self):
        return f'I am a {self.type}'

print(Cat('Hairball'))