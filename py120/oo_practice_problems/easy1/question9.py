'''

There are several variables listed below. What are the different variable types and 
how do you know which is which?

excited_dog = 'excited dog'
self.excited_dog = 'excited dog'
self.__class__.excited_dog = 'excited dog'
BigDog.excited_dog = 'excited dog'

The first one is just a local variable
the next is an instance variable given the rpefix self.
the next is a class variable given  __class__ in the middle
and the last one I would imagine is a class variable

hough not shown here, there are three other ways to access class variables:

You can use a cls. prefix inside class methods.
You can use a type(self). prefix when self is an instance of the class or one of its subclasses.
You can sometimes use a self. prefix when self is an instance of the class or one of its subclasses. However, this is not good practice and should be shunned.

'''