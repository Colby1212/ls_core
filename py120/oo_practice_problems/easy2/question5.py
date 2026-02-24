'''
Modify this code from the previous quesion so that calling Hello.hi() on the class (rahter than an instance)
still uses Greeting's instance method greet() to print 'Hi'

'''

class Hello:
    def hi(self):
        self.greet('Hello')

#Make sure you define the class method after
#Theinstance method. IF oyu try it the other way, the question
#below will prove a bit challending.


    @classmethod
    def hi(cls):
        greeting = Greeting()
        greeting.greet("Hi")

'''
What happens when you try to re-run snippet1? why do you think that is?

The problem now is that we have a class method, and an instance method
with the same name in a class. If you try to use an instance of a class method
to call the instance method, Python will call the class method instead. 

'''
