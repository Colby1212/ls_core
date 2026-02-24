'''
What would happen if you ran the following code?

class Television:
    @classmethod
    def manufacturer(cls):
        return 'Amazon'

    def model(self):
        return 'Omni Fire'

tv = Television()

print(tv.manufactuerer())
print(tv.model())
print(Television.manufacturer())


When we invoke tv.manufacturer, Python actually calls the class method
Television.manufacturer. This occurs since python lets you call class methods
using an instance object. This is tremendously confusing, but its something we tolerate
tv.manufactuerer() would return 'Amazon'

Invoking tv.model is easier to understand. You have a Television instance object
that you are using to call the instance method Television,model. This returns omni fire

When we call Television.model, we're trying to invoke an instance method though it were 
a class method. That simply doesn't work. So we get TypeError. The error
message is a bit hard to understand, but basically measn that you're calling a class method
as an instance method. 
