from pygame import *
from pygame.locals import *
import pygame
import time
from Node import *
from Getcenter import *

bg = pygame.image.load('content\\nameinput.png')
bg1 = pygame.image.load('content\\nameinput1.png')


def name(list,screen,width,height):
    l = list
    newlist = Empty
    name = ""
    font = pygame.font.Font(None, 50)
    playercount = 1
    screen.blit(bg1, (0,0))
    while not l.IsEmpty:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    if len(name) <= 11:
                        name += event.unicode
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.key == K_RETURN:
                    newlist = Node(name, newlist)
                    name = ""
                    l = l.Tail
                    if not l.IsEmpty:
                        playercount += 1
                    else:
                        return newlist

            playerindic = font.render("Type player " + str(playercount) + " name:", True, (0,0,0))
            
            block = font.render(name, True, (0, 0, 0))
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            screen.blit(playerindic, (GetCenter(width,height,playerindic)[0], GetCenter(width,height,playerindic)[1] - (height / 6)))
            #if len(name) == 0:
                #noEmpty = font.render("Name cant be empty", True, (0,0,0))
                #screen.blit(noEmpty, (GetCenter(width, height, noEmpty)[0], GetCenter(width, height, noEmpty)[1] - (height / 8)))
            if len(name) == 12:             
                errormsg = font.render("Max name length has been reached", True, (0,0,0))
                screen.blit(errormsg, (GetCenter(width,height,errormsg)[0], GetCenter(width,height,errormsg)[1] - (height / 8)))
            pygame.display.flip()
