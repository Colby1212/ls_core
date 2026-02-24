class SmartLamp:
    def __init__(self, color, brightness):
        self._color = color
        self._brightness = brightness

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        if not isinstance(color, str):
            raise TypeError('Color must be a string')
        
        self._color = color

    @property
    def brightness(self):
        return self._brightness
    
    @brightness.setter
    def brightness(self, brightness):
        if isinstance(brightness, int):
            if 0<= brightness <= 100:
                self._brightness = brightness
                return
        raise ValueError('Brightness must be between 0 and 100')
    
    def glow(self):
        return f'The lamp glows {self.color} with brightness {self.brightness}%'

lamp = SmartLamp('blue', 70)
print(lamp.color)      # blue
print(lamp.brightness) # 70
print(lamp.glow())     # The lamp glows blue with brightness 70%.

lamp.color = 'red'
lamp.brightness = 90
print(lamp.color)      # red
print(lamp.brightness) # 90
print(lamp.glow())     # The lamp glows red with brightness 90%.

lamp.brightness = 120
# ValueError: Brightness must be between 0 and 100.