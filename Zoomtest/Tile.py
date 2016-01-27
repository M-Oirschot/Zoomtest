import pygame
from Node import *

#Tile properties
notTraversable = 0
startingTile = 1
fighterTile = 2
normalTile = 3
cardStack = 4

class Tile:
    def __init__(self,position, properties):
        self.left = None
        self.up = None
        self.right = None
        self.down = None

        self.props = properties

    #def Draw(self, screen):
    #    pygame.draw.rect()

def build_square_board(dimension, tileSize):
    if(dimension % 2 == 0):
        #dimension should be uneven for the board to be generated
        return("Given dimension should be uneven.")
    else:
        possibleEntry = None
        node = Empty
        finalVar = ""
        for row in range(dimension):
            for column in range(dimension):
                if(row == 0 or row == dimension-1):
                    if(column == 0 or column == dimension-1):
                        properties = Node(startingTile, Empty)
                        node = Tile((column, row), properties)
                        possibleEntry = node
                    elif(column == (dimension-1)/2):
                        properties = Node(fighterTile, Empty)
                        node = Tile((column, row), properties)
                    else:
                        properties = Node(normalTile, Empty)
                        node = Tile((column, row) , properties)
                elif(row == (dimension-1)/2):
                    if(column == (dimension-1)/2):
                        #Cards tile
                        properties = Node(cardStack, Empty)
                        node = Tile((column, row), properties)
                    elif(column == 0 or column == dimension-1):
                        properties = Node(fighterTile, Empty)
                        node = Tile((column, row), properties)
                    else:
                        finalVar += " "
                else: 
                    if(column == 0):
                        properties = Node(normalTile, Empty)
                        node = Tile((column, row), properties)
                    elif(column == dimension-1):
                        properties = Node(normalTile, Empty)
                        node = Tile((column, row), properties)
                    else:
                        finalVar += " "
        return(node)
