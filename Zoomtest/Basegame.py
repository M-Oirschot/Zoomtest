﻿import pygame
from Dice import *
from Tile import *
from Node import *
from GetRandomEvent import *
from PickChoiceOverlay import *
from fightrules import *
from Getcenter import *
import sys

white = (255, 255, 255)
blue=(0,0,255)

pygame.init()
font = pygame.font.Font("content\\font\\fipps.TTF", 15)
playerName = font.render("Name:", 1, (255,255,0))
Condition = font.render("Condition:  4", 1, (255,255,0))


helpBtn = pygame.image.load("content\\helpbtn.png")
scBtn = pygame.image.load("content\\scoreBoardbtn.png")
rollDiceBtn = pygame.image.load("content\\rollDiceBtn.png")

def Menushit(screen,width,height,players,list,fighterlist,board,bg):
    if players == 2:
      player1 = list.Value
      player2 = list.Tail.Value
      player = [player1,player2]
      startingtiles = [20,0]
    elif players == 3:
      player1 = list.Value
      player2 = list.Tail.Value
      player3 = list.Tail.Tail.Value
      player = [player1,player2,player3]
      startingtiles = [10,20,0]
    elif players == 4:
      player1 = list.Value
      player2 = list.Tail.Value
      player3 = list.Tail.Tail.Value
      player4 = list.Tail.Tail.Tail.Value
      player = [player1,player2,player3,player4]
      startingtiles = [30,10,20,0]
    done = False
    first = True


    while not done:
        screen.blit(bg, (0,0))
        
        
       

        for i in range (0, len(player)):
            screen.blit(player[i].Texture, player[i].Tile.pos)
        pygame.display.flip()
        for i in range (0, len(player)):
            while True:
                playeronturn = font.render("It's " + player[i].Name + "'s turn!", 1, (255,255,0))
                screen.blit(playeronturn, (GetCenter(width, height, playerName)[0] - (width / 2.5), GetCenter(width,height, playerName)[1] - (height / 2.4) + 30))
                screen.blit(helpBtn,(GetCenter(width, height, helpBtn)[0] - (width / 3.525), GetCenter(width,height, helpBtn)[1] - (height / 3.525)))
                screen.blit(scBtn,(GetCenter(width, height, scBtn)[0] - (width / 2.4), GetCenter(width,height, scBtn)[1] - (height / 3.525)))
                screen.blit(rollDiceBtn,(GetCenter(width, height, rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height, rollDiceBtn)[1] - (height / 3)))
                pygame.event.get()
                pygame.display.flip()
                if (pygame.mouse.get_pressed()==(1,0,0) and helpBtn.get_rect(topleft=(GetCenter(width, height, rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height, rollDiceBtn)[1] - (height / 3))).collidepoint(pygame.mouse.get_pos())):
                    diceroll = dice(6)  
                    drawDice(diceroll,width, height, screen)
                    for k in range (0, diceroll):
                        if player[i].Pos == 39:
                            player[i].Pos = 0
                            player[i].Tile = board.Value
                        else:
                            player[i].Pos += 1
                            player[i].Tile = getItemFromList(board, player[i].Pos, 0)
                        screen.blit(bg, (0,0))
                        for j in range (0, len(player)):
                            screen.blit(player[j].Texture, player[j].Tile.pos)
                        #screen.blit(pygame.image.load("content\\" + str(diceroll) + ".png"), (GetCenter(width, height, diceImg)[0] - (width / 3), GetCenter(width,height, diceImg)[1] + (height / 3)))
                        time.sleep(0.4)
                        pygame.display.flip()
                    
                    break

                    
            if player[i].Pos == 5 or player[i].Pos == 15 or player[i].Pos == 25 or player[i].Pos == 35:
                superfight(player[i], PlayerversusSuperfight(screen,width,height,player[i],fighterlist))
                screen.blit(bg, (0,0))
                for i in range (0, len(player)):
                    screen.blit(player[i].Texture, player[i].Tile.pos)
            #for m in range (0, len(startingtiles)):
            #    if player[i].Pos == startingtiles[m]:
            #        pvp(player[i],player[m], PlayerversusPlayer(screen,width,height,player[i],player[m]))
                    
            
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
        """time.sleep(0.5)
        for i in range (0, len(player)):
          if player[i].Pos == 39:
            player[i].Pos = 0
            player[i].Tile = board.Value
          else:
            player[i].Pos += 1
            player[i].Tile = getItemFromList(board, player[i].Pos, 0)"""
        

def Main(screen,width,height,players,list,board):
    pygame.mixer.music.fadeout(1000)
    bg = pygame.transform.scale(pygame.image.load("content\\bordspel_background.png"), (width,height))
    templist = MakeList()
  
    

    #while not asdf.IsEmpty:
    #    print(asdf.Value.pos)
   #     asdf = asdf.Tail

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
        Menushit(screen,width,height,players,list,templist,board,bg)
          
