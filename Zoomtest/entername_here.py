from pygame import *
from pygame.locals import *
import pygame
import time
from Node import *
from Getcenter import *

def name(list,screen,width,height):
    l = list
    name = ""
    font = pygame.font.Font(None, 50)
    playercount = 1
    while not l.IsEmpty:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == K_BACKSPACE:
                    name = name[:-1]
                elif event.key == K_RETURN:
                    l.Value = name   #edit naar l.value.player.name
                    name = ""
                    l = l.Tail
                    if not l.IsEmpty:
                      playercount += 1
            #elif evt.type == QUIT:
            #    pygame.quit()
            screen.fill ((100, 100, 100))
            playerindic = font.render("Player " + str(playercount) + " Name:", True, (0,0,0))
            
            block = font.render(name, True, (0, 0, 0))
            rect = block.get_rect()
            rect.center = screen.get_rect().center
            screen.blit(block, rect)
            screen.blit(playerindic, (GetCenter(width,height,playerindic)[0], GetCenter(width,height,playerindic)[1] - (height / 6)))
            pygame.display.flip()


