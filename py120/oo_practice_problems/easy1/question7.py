'''

Suppose you have th Oracle class from above and a RoadTrip class that inherits from the Oracle class, as shown below:

import random

class Oracle:
    def predict_the_future(self):
        return f'You will {random.choice(self.choices())}.'


    def choices(self):
        return[
            'eat a nice lunch',
            'take a nap soon',
            'stay at work late',
            'adopt a cat',
            ]


class RoadTrip(Oracle):
    def choices(self):
        return[
            'visit Vegas',
            'fly to Fiji',
            'romp in Rome',
            'go on a Scrabble cruise',
            'get hopelessly lost',
            ]

What will happen? 

Because our choices method masks the choices method from our super class, instead it will return one of the 5 nessages in 
RoadTrip's choices method

'''