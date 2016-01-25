import random
 
class Player:
    def __init__(self, x, y, lifepoints, conditionpoints, texture, name):
        self.Y = y
        self.X = x
        self.Lifepoints = lifepoints
        self.Conditionpoints = conditionpoints
        self.Texture = texture
        self.Name = name