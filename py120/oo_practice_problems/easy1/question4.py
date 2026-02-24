'''

In the previous question, we had a mix-in called
SpeedMixin that contained go_fast method. When we call small_car.go_fast, you may have noticed that the output includes the vehicle type. 
How is this done.

This is because we created f strings and performed interpolation. in the curly brackets we have self.__class__.__name__
this provides the name of the class. 

1. self refers to the obect referenced by small_car (Car object)
2. self.__class__ returns a reference to the Car class, which is an object of the type class.
finally self.__class__.__name__ returns the name of the Car class as a string 'Car'

'''