First it would look within the class itself to look for the method, then it would look from right to left classes it inherits from and starts looking 
from inside to out. When it find nothing from the classes it inherits from, it will look at the object class and then finally if still nothing it return AttributeError


Lets say we are looking for Bulldog.drool (the bulldog class from the first problem) it will look at Bulldog.Drool, then Dog.Drool, then Pet.drool, then Object.droll. 
and again if it finds nothing it will return AttributeError

mro can be found using the mro class method

using mro is not very pretty, instead you can use a list comprehension to make the output more readable

print([cls.__name__ for cls in Bulldog.mro()])