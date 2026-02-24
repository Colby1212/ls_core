'''
supose we have this code:

class Greeting:
    def greet(Self, message):
        print(message)

class Hello(Greeting):
    def hi(self):
        self.greet("Hello")


class Goodbye(Greeting):
    def bye(self):
        self.greet("Goodbye")

without running the code, what would each sniiet do were you to run it?



Goodbye and Hello are both subclasses of greeting.

They both have access to the greet method defined in Greeting


snippet1:
hello = Hello()
hello.hi()
This creates an instance of Hello and calls the hi method, printing 'Hello'

snippet2:
hello = Hello()
hell.bye()
This would raise an AttributeError as the Hello class does not have a bye method.

snippet3:

hello = Hello()
hello.greet()
This creates an instance of Hello and calls the greet method, but with no argument
it would raise a TypeError because greet expects one agrument but none are given 

snippet4:

hello.Hello()
hello.greet("Goodbye")
This would print 'Goodbye'

snippet5:
Hello.hi()

This raises a TypeError because hi is missing one positional argument for
the self parameter. This happensbecause we're invoking hi on the class
Hello rather than an instance. When we invoke instance methods as class methods, no instance is passed
in as self. 

'''