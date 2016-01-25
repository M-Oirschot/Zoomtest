import random
def dice(sides):
    return random.randint(1, sides)

def diceGame(p1, p2, sides):
    rollOne = dice(sides)
    rollTwo = dice(sides)
    if rollOne > rollTwo:
        return(p1)
    elif rollTwo > rollOne:
        return(p2)
    else:
        return("draw")