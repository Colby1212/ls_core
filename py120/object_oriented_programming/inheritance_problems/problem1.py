''' 
GIven this class:

class Dog:
    def speak(self):
        return 'Bark!'

    def sleep(self):
        return 'sleeping'

teddy = Dog()
print(teddy.speak())
print(teddy.sleep())

One problem is that we need to keep track of different breeds of dogs since they have slightly different behaviors. 
For exmaple, bulldogs snore when they sleep, nut others do not
Create a subclass from Dog called bulldog overriding the sleep method to return 

'''

class Dog:
    def speak(self):
        return 'Bark!'
    
    def sleep(self):
        return 'Sleeping'

class Bulldog(Dog):
    def sleep(self):
        return 'Snoring!'

teddy = Bulldog()
print(teddy.speak())
print(teddy.sleep())