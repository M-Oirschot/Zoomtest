import pygame
from Node import *

#Tile properties
notTraversable = 0
startingTile = 1
fighterTile = 2
normalTile = 3

class Tile:
    def __init__(self,position, coords, properties):
        self.left = None
        self.up = None
        self.right = None
        self.down = None

        self.co = coords

        self.pos = position
        self.props = properties

def build_square_board(dimension, offset):
   
    possibleEntry = None
    node = Empty

    finalVar = ""
    for row in range(dimension):
        tRow = 34
        for column in range(dimension):
            tCol = 34
            if(row == 0 or row == dimension-1):
                if(column == 0 or column == dimension-1):
                    properties = Node(startingTile, Empty)
                    node = Node(Tile((column, row), (tCol, tRow), properties), node)
                    possibleEntry = node
                elif(column == (dimension-1)/2):
                    properties = Node(fighterTile, Empty)
                    node = Node(Tile((column, row), (tCol, tRow), properties), node)
                else:
                    properties = Node(normalTile, Empty)
                    node = Node(Tile((column, row), (tCol, tRow), properties), node)
            elif(row == (dimension-1)/2):
                if(column == 0 or column == dimension-1):
                    properties = Node(fighterTile, Empty)
                    node = Node(Tile((column, row), (tCol, tRow), properties), node)
                else:
                    finalVar += " "
            else: 
                if(column == 0):
                    properties = Node(normalTile, Empty)
                    node = Node(Tile((column, row), (tCol, tRow), properties), node)
                elif(column == dimension-1):
                    properties = Node(normalTile, Empty)
                    node = Node(Tile((column, row), (tCol, tRow), properties), node)
                else:
                    finalVar += " "
    return(node)
