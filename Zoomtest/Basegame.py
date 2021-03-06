﻿import pygame
from Dice import *
from Tile import *
from Node import *
from GetRandomEvent import *
from PickChoiceOverlay import *
from fightrules import *
from Player import *
from winScreenOverlay import *
from Getcenter import *
import sys

white = (255, 255, 255)
blue=(0,0,255)

pygame.init()
font = pygame.font.Font("content\\font\\retro.ttf", 35)
statfont = pygame.font.Font("content\\font\\retro.ttf", 25)
playerName = font.render("Name:", 1, (255,255,0))
Condition = font.render("Condition:  4", 1, (255,255,0))
helpBtn = pygame.image.load("content\\rules.png")
helpBtnh = pygame.image.load("content\\rules_h.png")
rollDiceBtn = pygame.image.load("content\\rolldice.png")
rollDiceBtnh = pygame.image.load("content\\rolldice_h.png")
pausebutton = pygame.image.load("content\\pause.png")
pausebuttonh = pygame.image.load("content\\pause_h.png")

def Menushit(screen,width,height,players,list,fighterlist,board,bg,mute):
    if players == 2:
        player1 = list.Value
        player2 = list.Tail.Value
        player = [player1,player2]
        startingTiles = [0,20]
    elif players == 3:
        player1 = list.Value
        player2 = list.Tail.Value
        player3 = list.Tail.Tail.Value
        player = [player1,player2,player3]
        startingTiles = [0,20,10]
    elif players == 4:
        player1 = list.Value
        player2 = list.Tail.Value
        player3 = list.Tail.Tail.Value
        player4 = list.Tail.Tail.Tail.Value
        player = [player1,player2,player3,player4]
        startingTiles = [0,20,10,30]
    done = False
    first = True

    while not done:
        tempvar = removeDead(player,startingTiles)
        player = tempvar[0]
        startingTiles = tempvar[1]
        screen.blit(bg, (0,0))
        if len(player) == 1:
            return player[0].Name
            break
        pygame.display.flip()
        for i in range (0, len(player)):
            done = True
            while done == True:
                screen.blit(bg, (0,0))
                if len(player) == 1:
                    return player[0].Name
                    break
                playersStandingOnSameTile = checkPlayers(player)
                if len(playersStandingOnSameTile) != 0:
                    offset = 0
                    for m in range (0, len(playersStandingOnSameTile)):
                        if playersStandingOnSameTile[m].Lifepoints > 0:
                            screen.blit(playersStandingOnSameTile[m].Texture, (playersStandingOnSameTile[m].Tile.pos[0] + offset, playersStandingOnSameTile[m].Tile.pos[1]))
                            offset += 10
                    for j in range (0, len(player)):
                        if player[j] not in playersStandingOnSameTile:
                            if player[j].Lifepoints > 0:
                                screen.blit(player[j].Texture, player[j].Tile.pos)
        
        
                else:
                    for j in range (0, len(player)):
                        if player[j].Lifepoints > 0:
                            screen.blit(player[j].Texture, player[j].Tile.pos)
                printVisuals(player,screen,width,height)
                playeronturn = font.render(player[i].Name + "'s turn", 1, (0,0,0))
                screen.blit(playeronturn, (GetCenter(width, height, playerName)[0] - (width / 3) - 80, GetCenter(width,height, playerName)[1] - (height / 2.4) - 15))
                screen.blit(player[i].Texture, (GetCenter(width, height, playerName)[0] - (width / 2.1) + 45, GetCenter(width,height, playerName)[1] - (height / 2.4) - 20))
                screen.blit(helpBtn,(GetCenter(width, height, rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15))
                screen.blit(rollDiceBtn,(GetCenter(width, height, rollDiceBtn)[0] - (width / 6) + 20 , GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15))
                screen.blit(pausebutton,(GetCenter(width, height, pausebutton)[0] - (width / 3.5) , GetCenter(width,height, pausebutton)[1] - (height / 3.5) + 15))

                if rollDiceBtn.get_rect(topleft=(GetCenter(width, height, rollDiceBtn)[0] - (width / 6) + 20 , GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15)).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(rollDiceBtnh,(GetCenter(width, height, rollDiceBtn)[0] - (width / 6) + 20 , GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15))
                if helpBtn.get_rect(topleft=(GetCenter(width, height, rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15)).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(helpBtnh,(GetCenter(width, height, rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15))
                if pausebutton.get_rect(topleft=(GetCenter(width, height, pausebutton)[0] - (width / 3.5) , GetCenter(width,height, pausebutton)[1] - (height / 3.5) + 15)).collidepoint(pygame.mouse.get_pos()):
                    screen.blit(pausebuttonh,(GetCenter(width, height, pausebutton)[0] - (width / 3.5) , GetCenter(width,height, pausebutton)[1] - (height / 3.5) + 15))

                pygame.event.get()
                pygame.display.flip()
                if (pygame.mouse.get_pressed()==(1,0,0) and rollDiceBtn.get_rect(topleft=(GetCenter(width, height, rollDiceBtn)[0] - (width / 6) + 20 , GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15)).collidepoint(pygame.mouse.get_pos())):
                    diceroll = dice(6)  
                    drawDice(diceroll,width, height, screen)
                    time.sleep(0.5)
                    for k in range (0, diceroll):
                        if player[i].Pos == 39:
                            player[i].Pos = 0
                            player[i].Tile = board.Value
                        else:
                            player[i].Pos += 1
                            player[i].Tile = getItemFromList(board, player[i].Pos, 0)
                        if player[i].Pos == startingTiles[i]:
                            player[i].Lifepoints += 10
                            player[i].Conditionpoints = 15
                            printVisuals(player,screen,width,height)
                        diceImg = pygame.image.load("content\\" + str(diceroll) + ".png")
                        screen.blit(bg, (0,0))
                        screen.blit(diceImg, (GetCenter(width, height, diceImg)[0] - (width / 10), GetCenter(width,height, diceImg)[1] - ((height / 2) -80)))
                        playersStandingOnSameTile = checkPlayers(player)
                        if len(playersStandingOnSameTile) != 0:
                            offset = 0
                            for m in range (0, len(playersStandingOnSameTile)):
                                screen.blit(playersStandingOnSameTile[m].Texture, (playersStandingOnSameTile[m].Tile.pos[0] + offset, playersStandingOnSameTile[m].Tile.pos[1]))
                                offset += 10
                            for j in range (0, len(player)):
                                if player[j] not in playersStandingOnSameTile:
                                    if player[j].Lifepoints > 0:
                                        screen.blit(player[j].Texture, player[j].Tile.pos)
                        else:
                            for j in range (0, len(player)):
                                if player[j].Lifepoints > 0:
                                    screen.blit(player[j].Texture, player[j].Tile.pos)


                        time.sleep(0.2)
                        pygame.display.flip()
                    done = False
                    break
                if (pygame.mouse.get_pressed() == (1,0,0) and helpBtn.get_rect(topleft=(GetCenter(width, height, rollDiceBtn)[0] - (width / 2.4), GetCenter(width,height, rollDiceBtn)[1] - (height / 3.5) + 15)).collidepoint(pygame.mouse.get_pos())):
                    showrules()

                if (pygame.mouse.get_pressed() == (1,0,0) and pausebutton.get_rect(topleft=(GetCenter(width, height, pausebutton)[0] - (width / 3.5) , GetCenter(width,height, pausebutton)[1] - (height / 3.5) + 15)).collidepoint(pygame.mouse.get_pos())):
                    if pauseScreen(screen, width, height)==1:
                        return 1
                        break
                        

            if player[i].Pos in startingTiles and player[i].Pos != startingTiles[i]:
                pvp(player[i],player[startingTiles.index(player[i].Pos)], PlayerversusPlayer(screen,width,height,player[i],player[startingTiles.index(player[i].Pos)]))
                screen.blit(bg, (0,0)) 
            if player[i].Pos == 5 or player[i].Pos == 15 or player[i].Pos == 25 or player[i].Pos == 35:
                superfight(player[i], PlayerversusSuperfight(screen,width,height,player[i],fighterlist))
                screen.blit(bg, (0,0))
                for i in range (0, len(player)):
                    screen.blit(player[i].Texture, player[i].Tile.pos)
            checkPvp(player,screen,width,height,player[i])
            if len(player) == 1:
                return player[0].Name
                break
            pygame.display.flip()
        pygame.event.get()
 
        pygame.display.flip()
             
def Main(screen,width,height,players,list,board,mute):
    bg = pygame.transform.scale(pygame.image.load("content\\board.png"), (width,height))
    templist = MakeList()
  
    while True:
        screen.fill(white)
        screen.blit(bg, (0, 0))
        diceImg = pygame.image.load("content\\" + str(dice(6)) +".png")
        screen.blit(diceImg, (GetCenter(width, height, diceImg)[0] - (width / 10), GetCenter(width,height, diceImg)[1] - ((height / 2) -80)))

        pygame.display.flip()
        tempusvar = Menushit(screen,width,height,players,list,templist,board,bg,mute)
        if tempusvar != 1:
          winScreen(screen,width,height,tempusvar)
        break
    

def playerstats(player):
    while True:
        player1health = font.render(player[1].Lifepoints, 1, (0,0,0))
        player1stamina = font.render(player[1].Conditionpoints, 1, (0,0,0))
        screen.blit(player1health, (GetCenter(width, height, player1health)[0] - (width / 3), GetCenter(width,height, player1health)[1] - (height / 2.4) - 15))
