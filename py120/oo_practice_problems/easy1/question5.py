'''
Which of the following classes would create objects that have an instance variable?
How do you know

class Fruit:
    def __init__(self, name):
        my_name = name

class Pizza:
    def __init__(self, name):
        self.my_name = name

Here only the Pizza class would create an instance variable. We know this because in the pizza.__init__ we have
self.my_name = name which by virtue creates an instance variable. 

Although the fruit class instead has a local variable only defined inside Fruit.__init__ (no self.)


print(vars(Fruit('orange')))     # {}
print(vars(Pizza('pepperoni')))  # {'my_name': 'pepperoni'}

In this example, we can see that the Fruit object has no instance variables,
 while the Pizza object has a my_name instance variable whose value is 'pepperoni'.
'''