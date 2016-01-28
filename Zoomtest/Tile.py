﻿import pygame
from Node import *

#Tile properties
notTraversable = 0
startingTile = 1
fighterTile = 2
normalTile = 3

class Tile:
    def __init__(self,position, coords, startingTile):
        self.sTile = False
        self.co = coords
        self.pos = position

def build_square_board(dimension, offset):
   
    possibleEntry = None
    node = Empty
    
    finalVar = ""
    '''
    for row in range(dimension):
        tRow = 600 * row
        for column in range(dimension):
            if column == 0:
                tCol = 300
            else:
                tCol = 300 * column
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
    '''

    standardOffset = 850
    coordinates = Empty
    x = 915
    y = 20
    colOffset = 600
    rowOffset = 200

    for firstRow in range(dimension):
        tRow = firstRow * rowOffset + standardOffset
        for lastColumn in range (dimension):
            tCol = lastColumn * colOffset
            if(firstRow == 0):
                if(lastColumn == 0):
                    node = Node(Tile((lastColumn, firstRow), (x, y), True), node)
                    x += 156
                elif(lastColumn == dimension-1):
                    node = Node(Tile((lastColumn, firstRow), (x, y), True), node)
                    x += 78
                elif(lastColumn == 5):
                    x += 39
                    node = Node(Tile((lastColumn, firstRow), (x, y), False), node)
                    x += 117
                else:
                    node = Node(Tile((lastColumn, firstRow), (x, y), False), node)
                    x += 78

            elif(lastColumn == dimension-1):              
                if(firstRow == 1):
                    node = Node(Tile((lastColumn, firstRow), (x, y), False), node)

                elif(firstRow == 5):
                    node = Node(Tile((lastColumn, firstRow), (x, y), False), node)
                    y += 117
                elif(firstRow == dimension-1):
                    node = Node(Tile((lastColumn, firstRow), (x, y), True), node)

                else:
                    node = Node(Tile((lastColumn, firstRow), (x, y), True), node)


    for lastRow in range(dimension, 0, -1):
        for firstColumn in range(dimension, 0, -1):

            if(lastColumn == dimension-1):
                if(firstRow == dimension-1):
                    node = Node(Tile((firstColumn, lastRow), (0, 0), True), node)
                elif(firstrow > 1 and firstRow <= 9):
                    node = Node(Tile((firstColumn, lastRow), (0, 0), False), node)
                else:
                    node = Node(Tile((firstColumn, lastRow), (0, 0), True), node)

    return(node)

