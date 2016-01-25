﻿import pygame
from Dice import *
from Tile import *
from Getcenter import *
import sys

white = (255, 255, 255)


pygame.init()
font = pygame.font.Font(None, 20)
playerName = font.render("Name:        Wesselt", 1, (255,255,0))
Condition = font.render("Condition:  4", 1, (255,255,0))

helpBtn = pygame.image.load("content\\helpbtn.png")
scBtn = pygame.image.load("content\\scoreBoardbtn.png")
rollDiceBtn = pygame.image.load("content\\rollDiceBtn.png")

def Menushit(screen,width,height):
    players = 0
    done = False
    while not done:
        
        screen.blit(helpBtn,(GetCenter(width, height, playerName)[0] - (width / 3.525), GetCenter(width,height, playerName)[1] - (height / 3.525)))
        screen.blit(scBtn,(GetCenter(width, height, playerName)[0] - (width / 2.4), GetCenter(width,height, playerName)[1] - (height / 3.525)))
        screen.blit(rollDiceBtn,(GetCenter(width, height, playerName)[0] - (width / 2.4), GetCenter(width,height, playerName)[1] - (height / 3)))
           
        """pygame.event.get()

        if (pygame.mouse.get_pressed()==(1,0,0)) and players == 0 and helpBtn.get_rect(center=(425,450)).collidepoint(pygame.mouse.get_pos()):
            players += 2
            done = True
        elif (pygame.mouse.get_pressed()==(1,0,0)) and players == 0 and scBtn.get_rect(center=(425,550)).collidepoint(pygame.mouse.get_pos()):
            players += 3
            done = True
        elif (pygame.mouse.get_pressed()==(1,0,0)) and players == 0 and rollDiceBtn.get_rect(center=(425,550)).collidepoint(pygame.mouse.get_pos()):
            players += 3
            done = True"""
        pygame.display.flip()

def Main(screen,width,height):
    bg = pygame.transform.scale(pygame.image.load("content\\bordspel_background.png"), (width,height))
    while True:
        screen.fill(white)
        screen.blit(bg, (0, 0))
        screen.blit(playerName, (GetCenter(width, height, playerName)[0] - (width / 2.5), GetCenter(width,height, playerName)[1] - (height / 2.2)))
        screen.blit(Condition, (GetCenter(width, height, playerName)[0] - (width / 2.5), GetCenter(width,height, playerName)[1] - (height / 2.4)))
        
        diceImg = pygame.image.load("content\\" + str(dice(6)) +".png")
        screen.blit(diceImg, (GetCenter(width, height, playerName)[0] - (width / 2.4), GetCenter(width,height, playerName)[1] + (height / 2.825)))

        sys.stdout.write(build_square_board(10,5))
        print("")
        pygame.display.flip()
        Menushit(screen,width,height)
      

        