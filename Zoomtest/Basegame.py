import pygame
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
font = font = pygame.font.Font("content\\font\\fipps.TTF", 15)
playerName = font.render("Name:", 1, (255,255,0))
Condition = font.render("Condition:  4", 1, (255,255,0))

helpBtn = pygame.image.load("content\\helpbtn.png")
scBtn = pygame.image.load("content\\scoreBoardbtn.png")
rollDiceBtn = pygame.image.load("content\\rollDiceBtn.png")

def Menushit(screen,width,height,players,list,fighterlist,board,listofcoordinates,bg):
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
    first = True

    asdfg = sadf
    for i in range (0, len(player)):
        while not asdfg.IsEmpty:
            if asdfg.Value.playerOneBase == True:
                player[0].Pos = asdfg.Value 
            if asdfg.Value.playerTwoBase == True:
                player[1].Pos = asdfg.Value
            if asdfg.Value.playerOneBase == True:
                player[2].Pos = asdfg.Value
            if asdfg.Value.playerOneBase == True:
                player[3].Pos = asdfg.Value  
            asdfg = asdfg.Tail        

    while not done:
        screen.blit(player[i].Texture, player[i].Pos.pos)
        """if first == True:
          superfight(player[0],PlayerversusSuperfight(screen,width,height,player[0],fighterlist))
          print(pvp(player[0],player[1],PlayerversusPlayer(screen,width,height,player[0],player[1])))
          first = False
        print(player[0].Name)
        print(player[0].Conditionpoints)
        print(player[0].Lifepoints)
        print(player[1].Name)
        print(player[1].Conditionpoints)
        print(player[1].Lifepoints)
        input()
        for i in range (0, len(player)):
            while not asdf.IsEmpty:
                if asdf.Value.playerOneBase:
                    player[1].Pos = asdf.Value 
            if asdf.Value.playerTwoBase:
                    player[2].Pos = asdf.Value
            if asdf.Value.playerOneBase:
                    player[3].Pos = asdf.Value
            if asdf.Value.playerOneBase:
                    player[4].Pos = asdf.Value  
            screen.blit(player[i].Texture, player[i].Pos.pos)
            coordinate = getItemFromList(listofcoordinates,player[i].Pos,0).pos
            if player[i].Pos == 5:
                    superfight(player[i], PlayerversusSuperfight(screen,width,height,player[i],fighterlist))      
             """  
        #print(player[0].Name, player[0].Pos)
        #print(getItemFromList(listofcoordinates,player[0].Pos,0).pos)
        #input()
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
        time.sleep(1)
        for i in range (0, len(player)):
          if player[i].Pos == 39:
            player[i].Pos = 0
          else:
            player[i].Pos += 1
        screen.blit(bg, (0,0))

def Main(screen,width,height,players,list,board):
    pygame.mixer.music.fadeout(1000)
    bg = pygame.transform.scale(pygame.image.load("content\\bordspel_background.png"), (width,height))
    templist = MakeList()

    tp = board
    
    asdf = Empty
    while not tp.IsEmpty:
        asdf = Node(tp.Value, asdf)
        tp = tp.Tail

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
        Menushit(screen,width,height,players,list,templist,board,asdf,bg)
          
