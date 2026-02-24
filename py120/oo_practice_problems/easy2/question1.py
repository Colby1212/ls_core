''' 

Suppose you have these two classes:

class Game:
    def play(self):
        return'STart the game!'

class Bingo:
    pass

Update this code so that bingo inherits the play method from the Game class

'''



class Game:
    def play(self):
        return'STart the game!'

class Bingo(game):
    pass

    