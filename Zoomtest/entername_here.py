from pygame import *
from pygame.locals import *
import pygame
import time
from Node import *
from Getcenter import *
import random

bg = pygame.image.load('content\\nameinput.png')
bg1 = pygame.image.load('content\\nameinput1.png')
poneF = pygame.image.load("content\\player4pion.png")
ptwoF = pygame.image.load("content\\player3pion.png")
pthreeF = pygame.image.load("content\\player2pion.png")
pfourF = pygame.image.load("content\\player1pion.png")
r = 222
g = 222
b = 222




def name(list,screen,width,height):

    memesquare = pygame.Surface((385,55), pygame.SRCALPHA, 32)
    othersquare = pygame.Surface((615,95), pygame.SRCALPHA, 32)
    memesquare.fill((r,g,b))
    othersquare.fill((r,g,b))
    l = list
    newlist = Empty
    name = ""
    font = pygame.font.Font("content\\font\\retro.ttf", 23)
    otherfont = pygame.font.Font("content\\font\\retro.ttf", 30)
    playercount = 1
    screen.blit(bg, (0,0))
    tempbool = False
    while not l.IsEmpty:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    if len(name) <= 11:
                        name += event.unicode
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.key == K_RETURN:

                    if len(name) != 0:
                        newlist = Node(name, newlist)
                        name = ""
                        l = l.Tail
                        if not l.IsEmpty:
                            playercount += 1
                            tempbool = False
                        else:
                            return newlist
                    else:
                      tempbool = True
            
            playerindic = font.render("Type player " + str(playercount) + " name:", True, (0,0,0))
            if playercount == 1:
              screen.blit(pygame.image.load("content\\player1pion.png"), (GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[0],GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[1] + (height / 8)))
            elif playercount == 2:
              screen.blit(pygame.image.load("content\\player3pion.png"), (GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[0],GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[1] + (height / 8)))
            elif playercount == 3: 
              screen.blit(pygame.image.load("content\\player2pion.png"), (GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[0],GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[1] + (height / 8)))
            else:
              screen.blit(pygame.image.load("content\\player4pion.png"), (GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[0],GetCenter(width,height,pygame.image.load("content\\player1pion.png"))[1] + (height / 8)))
            block = otherfont.render(name, True, (0, 0, 0))
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(memesquare, (GetCenter(width,height,memesquare)[0] + 1, GetCenter(width,height,memesquare)[1]))
            screen.blit(othersquare, (GetCenter(width,height,othersquare)[0] + 1, GetCenter(width,height,othersquare)[1] - 155 ))
            screen.blit(block, rect)
            screen.blit(playerindic, (GetCenter(width,height,playerindic)[0], GetCenter(width,height,playerindic)[1] - (height / 6)))
            if len(name) == 0 and tempbool == True:
                noEmpty = font.render("Name cant be empty", True, (0,0,0))
                screen.blit(noEmpty, (GetCenter(width, height, noEmpty)[0], GetCenter(width, height, noEmpty)[1] - (height / 8)))
            if len(name) == 12:             
                errormsg = font.render("Max name length has been reached", True, (0,0,0))
                screen.blit(errormsg, (GetCenter(width,height,errormsg)[0], GetCenter(width,height,errormsg)[1] - (height / 8)))
            pygame.display.flip()
