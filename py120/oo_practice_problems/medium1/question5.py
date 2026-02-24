'''

How could you change the light_status method name below so that the method name is clearer and less repetitive


class Light:
    def __init__(self, brightness, color):
        self.brightness = brightness
        self.color = color

    def light_status(self):
        return f'I have a brightness level of {self.brightness} and a color of {self.color}'

We can change the name to just status since it is already within the Light class context. This way we do not have to repeat
light in the mehtod name and well as the instance name. 

'''