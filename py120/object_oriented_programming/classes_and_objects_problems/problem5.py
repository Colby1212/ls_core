'''
Continuing with our Person class definition, what do you think the following code prints?

bob = Person('Robert Smith')
print(f'This person's name is: {bob}')

I think this would print 
"This person's name is Person('Robert Smith')"

output: The person's name is: <__main__.Person object at 0x100385f90>

We're using string interpolation in this code, as opposed to string concatenation. 
Python automatically calls the str function on the expression between the {}. 
Every object in Python responds to the str function which, by default, is inherited from the object class. 
By default, it prints out some gibberish, which represents the object's place in memory.

Until we learn how to override str's behavior, we must construct the output string in some other way. For instance, we can use:

print("The person's name is:" + bob.name)


we can override the str function for Person objects by defining a magic method, the __str__ method within the person class:

def __str__(self):
    return self.name

With the added magic function what will

bob = Person('Robert Smith')
print(f'This person's name is: {bob}')

output? 

I think it will output

"This person's name is: Robert Smith"
'''


print(type(22))