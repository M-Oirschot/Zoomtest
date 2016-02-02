import random
import pygame
import time
from Getcenter import *

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

def drawDice(roll,width,height,screen):
    diceImg = pygame.image.load("content\\" + str(roll) +".png")
    
    for i in range(0,random.randint(5,9)):
        screen.blit(pygame.image.load("content\\" + str(dice(6)) + ".png"), (GetCenter(width, height, diceImg)[0] - (width / 10), GetCenter(width,height, diceImg)[1] - ((height / 2) -80)))
        pygame.display.flip()
        floatmeme = float(random.randint(1,3) / 10)
        time.sleep(floatmeme)
    screen.blit(diceImg, (GetCenter(width, height, diceImg)[0] - (width / 10), GetCenter(width,height, diceImg)[1] - ((height / 2) -80)))
    pygame.display.flip()

def drawDiceBL(roll,width,height,screen):
    diceImg = pygame.image.load("content\\" + str(roll) +".png")
    
    for i in range(0,random.randint(5,9)):
        screen.blit(pygame.image.load("content\\" + str(dice(6)) + ".png"), (GetCenter(width, height, diceImg)[0] - (width / 3), GetCenter(width,height, diceImg)[1] + (height / 3)))
        pygame.display.flip()
        floatmeme = float(random.randint(1,3) / 10)
        time.sleep(floatmeme)
    screen.blit(diceImg, (GetCenter(width, height, diceImg)[0] - (width / 3), GetCenter(width,height, diceImg)[1] + (height / 3)))
    pygame.display.flip()