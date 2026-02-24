'''
lets practice creating an object hierarchy

create a class called Animal with a single instance method called spead that takes a string argument and prints
that argument to the terminal

Now create two other classes that inherit from Animal: Cat and Dog. 
The cat class should have a meow instance method that takes no argument and prints meow!
The fog class should have a bark instance method that says Woof Woof Woof. 
Make use of the Animal Class's speak method when implementing the Cat and Dog classes. Dont invoke the print function in either of the subclasses. 

'''


class Animal:
    def speak(self, message):
        print(message)


class Cat(Animal):
    def meow(self):
        self.speak('Meow!')

class Dog(Animal):
    def bark(self):
        self.speak(('Woof! ' * 3).strip())