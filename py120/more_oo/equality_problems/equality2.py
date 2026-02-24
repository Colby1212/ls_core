'''

Consider the following class:


class Cat:
    def __init__(self, name):
        self.name = name

Create the methods needed so you can compare Cat Objects for equality and inequality by their name value.
The comparison should ignore case and should work for the == and != operators. If the right-hand operand is not a Cat object,
THe methods should return NotImplemented

'''




class Cat:
    def __init__(self,name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() == other.name.casefold()

    def __ne__(self, other):
            if not isinstance(other, Cat):
                return NotImplemented
            return self.name.casefold() != other.name.casefold()

dog = Cat('Dog')
bird = Cat('Bird')

print(dog != bird)