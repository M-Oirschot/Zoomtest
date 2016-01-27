import pygame
from Dice import *
from Tile import *
from Node import *
from GetRandomEvent import *
from PickChoiceOverlay import *
from Getcenter import *
import sys

white = (255, 255, 255)
blue=(0,0,255)

pygame.init()
font = pygame.font.Font(None, 20)
playerName = font.render("Name:", 1, (255,255,0))
Condition = font.render("Condition:  4", 1, (255,255,0))

helpBtn = pygame.image.load("content\\helpbtn.png")
scBtn = pygame.image.load("content\\scoreBoardbtn.png")
rollDiceBtn = pygame.image.load("content\\rollDiceBtn.png")

def Menushit(screen,width,height,players,list,fighterlist):
    if players == 2:
      player1 = list.Value
      player2 = list.Tail.Value
      player = [player1,player2]
    elif players == 3:
      player1 = list.Value
      player2 = list.Tail.Value
      player3 = list.Tail.Tail.Value
      player = [player1,player2,player3]
    elif players == 4:
      player1 = list.Value
      player2 = list.Tail.Value
      player3 = list.Tail.Tail.Value
      player4 = list.Tail.Tail.Tail.Value
      player = [player1,player2,player3,player4]
    done = False
    while not done:
        screen.blit(helpBtn,(GetCenter(width, height, helpBtn)[0] - (width / 3.525), GetCenter(width,height, helpBtn)[1] - (height / 3.525)))
        screen.blit(scBtn,(GetCenter(width, height, scBtn)[0] - (width / 2.4), GetCenter(width,height, scBtn)[1] - (height / 3.525)))
        screen.blit(rollDiceBtn,(GetCenter(width, height, rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height, rollDiceBtn)[1] - (height / 3)))
           
        pygame.event.get()

        if (pygame.mouse.get_pressed()==(1,0,0) and helpBtn.get_rect(topleft=(GetCenter(width,height,rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height,rollDiceBtn)[1] - (height / 3))).collidepoint(pygame.mouse.get_pos())):
            print("done0")
            diceRoll = dice(6)
            diceImg = pygame.image.load("content\\" + str(dice(6)) +".png")
            print("done1")
            done = True
        if (pygame.mouse.get_pressed()==(1,0,0) and helpBtn.get_rect(topleft=(GetCenter(width,height,helpBtn)[0] - (width / 3.525), GetCenter(width,height,helpBtn)[1] - (height / 3.525))).collidepoint(pygame.mouse.get_pos())):
            print("Help")
            done = True

        pygame.display.flip()

def Main(screen,width,height,players,list):
    #pygame.mixer.music.fadeout(1000)
    bg = pygame.transform.scale(pygame.image.load("content\\bordspel_background.png"), (width,height))
    board = build_square_board(11,5)
    templist = MakeList()
    
    while True:
        screen.fill(white)
        screen.blit(bg, (0, 0))
        screen.blit(playerName, (GetCenter(width, height, playerName)[0] - (width / 2.5), GetCenter(width,height, playerName)[1] - (height / 2.2)))
        screen.blit(Condition, (GetCenter(width, height, playerName)[0] - (width / 2.5), GetCenter(width,height, playerName)[1] - (height / 2.4)))
        
        diceImg = pygame.image.load("content\\" + str(dice(6)) +".png")
        screen.blit(diceImg, (GetCenter(width, height, playerName)[0] - (width / 2.4), GetCenter(width,height, playerName)[1] + (height / 2.825)))

        pygame.draw.rect(screen,blue,(200,150,100,50))

        print("")
        pygame.display.flip()
        Menushit(screen,width,height,players,list,templist)
          
