'''
suppose you have the following class:
 
 class Cat:
    _cats_counts = 0

    def __init__(self, type):
        self.type = type
        self.__class__._cats_count += 1


    @class method
    def cats_count(cls):
        return cls.__cats__count


Explain what the _cats_count variable is, what it does in this class, and how it works. 

This is a class variable that tracks the amount of cat instances we have created. 
Given that there is a single underscore prefix this variable is for internal use only.
This variable increments every time we create a Cat object, we know this because in the class's __init__ method
we increment this variable by 1. 