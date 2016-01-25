#Tile properties
NotTraversable = 0
NormalTile = 1

class Tile:
    def __init__(self,position,texture):
        self.left = None
        self.up = None
        self.right = None
        self.down = None

def build_square_board(dimension, tileSize):
    entry_point = None
    prev_tile = None

    finalVar = ""
    for row in range(dimension):
        finalVar += "\n"
        for column in range(dimension):
            if(row == 0 or row == 9):
                if(column == 0 or column == 9):
                    finalVar += "+"
                else:
                    finalVar += "."
            else:
                if(column == 0):
                    finalVar += "|"
                elif(column == 9):
                    finalVar += "|"
                else:
                    finalVar += "X"
    return(finalVar)
