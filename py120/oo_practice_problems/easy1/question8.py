'''
Suppose you have an object named my_obj and that you want to call a method named foo using my_onj as the caller. 

How can you see where python will look for the method?
you don't need to determine the actualy method location; identifying the search sequence is sufficient


use the class.mro method (my_obj.__class__.mro()) This is defined by teh type calss, the superclass of all python classes


IF returns the method resolution order (MRO) for the class that invokes it. 

The output for mro() is a bit ugly to look at. if you want you can print itn more clearly, you can use a for loop and the __name__variabke)

for klass in my_obj.__class__.mro():
    print(klass.__name__)

The MRO is also called the lookup chain, since Python will look for a method starting int he first calss in teh chain, then the seocnd, and so on until it
gets to teh ultimate superclass (object). IF STILL no method, than python will raise AttributeError

'''