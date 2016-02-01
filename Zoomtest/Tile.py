import pygame
from Node import *
 
class Tile:
    def __init__(self,position, one, two, three, four, fight):
        self.pos = position
        self.playerOneBase = one
        self.playerTwoBase = two
        self.playerThreeBase = three
        self.playerFourBase = four
        self.sTile = fight          #superfight tile
 
def build_square_board(dimension, offset):
   
    node = Empty
    standardOffset = 850
    coordinates = Empty
    x = 853
    y = 20
    colOffset = 600
    rowOffset = 200
     
    for topRow in range(11):
        print("x: " + str(x) + "y: " + str(y))
        if topRow == 0:
            node = Node(Tile((x,y), True, False, False, False, False),node)
            x += 130
        elif topRow == 4:
            node = Node(Tile((x,y), False, False, False, False, False),node)
            x += 124
        elif topRow == 5:
            node = Node(Tile((x,y), False, False, False, False, True),node)
            x += 117
        elif topRow == 10:
            node = Node(Tile((x,y), False, True, False, False, False),node)
            y += 127
        else:
            node = Node(Tile((x,y), False, False, False, False, False),node)
            x  += 78
        
 
    for rightRow in range(9):
        print("x: " + str(x) + "y: " + str(y))
        if rightRow == 3:
            node = Node(Tile((x,y), False, False, False, False, False),node)
            y += 117
        elif rightRow == 4:
            node = Node(Tile((x,y), False, False, False, False, True), node)
            y += 124
        elif rightRow == 8:
            node = Node(Tile((x,y), False, False, True, False, False), node)
            y += 80
        else:
            node = Node(Tile((x,y), False, False, False, False, False), node)
            y += 78
        print("I ran " + str(rightRow))
        print("x: " + str(x) + "y: " + str(y))
 
    for bottomRow in range(10):
        print("x: " + str(x) + "y: " + str(y))
        if bottomRow == 4:
            node = Node(Tile((x,y), False, False, False, False, False), node)
            x -= 117
        elif bottomRow == 5:
            node = Node(Tile((x,y), False, False, False, False, True), node)
            x -= 124
        elif bottomRow == 9:
            node = Node(Tile((x,y), False, False, False, True, False), node)
            x -= 130
        else:
            node = Node(Tile((x,y), False, False, False, False, False), node)
            x -= 78
 
    for leftRow in range(10):
        print("x: " + str(x) + "y: " + str(y))
        if leftRow == 4:
            node = Node(Tile((x,y), False, False, False, False, False), node)
            y -= 117
        elif leftRow == 5:
            node = Node(Tile((x,y), False, False, False, False, True), node)
            y -= 117
        else:
            node = Node(Tile((x,y), False, False, False, False, False), node)
            y -= 78
 
    return(node)