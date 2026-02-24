'''
Using the answer to the previous problem, create the methods needed so you can perform ordered comparisons of Cat objects by their name value. 

As with the previous problem, the comparison should ignore case. They should work for the <, <-, >, and >= operators. 

If the right-hand operand is not a Cat object the methods should return NotImplemented

'''  

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() == other.name.casefold()


    def __ne__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() != other.name.casefold()

    def __gt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() > other.name.casefold()

    def __ge__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.casefold() >= other.name.casefold()


    def __lt__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented
        
        return self.name.casefold() < other.name.casefold()


    def __le__(self, other):
        if not isinstance(other, Cat):
            return NotImplemented

        return self.name.case() <= other.name.casefold()