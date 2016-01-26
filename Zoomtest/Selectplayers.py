import pygame
import time
from Getcenter import *
#pion = pygame.image.load('pion.png')
#bg= pygame.image.load('board.jpg')
font = pygame.font.Font(None, 50)
bg1 = pygame.image.load('content\\playerselect1.png')
bg = pygame.image.load('content\\playerselect.png')
titletext = font.render("Select amount of players:", 1,(0,0,0))
twoplayer = pygame.image.load('content\\2p.png')
twoplayerh = pygame.image.load('content\\2p_h.png')
threeplayer = pygame.image.load('content\\3p.png')
threeplayerh = pygame.image.load('content\\3p_h.png')
fourplayer = pygame.image.load('content\\4p.png')
fourplayerh = pygame.image.load('content\\4p_h.png')
 
def Playerselect(screen,width,height):
    
    screen.fill((100,100,100))
    screen.blit(bg1, (0,0))
    #screen.blit(titletext, (GetCenter(width,height,titletext)[0], GetCenter(width, height, titletext)[1] - 155))

    pygame.display.flip()
    time.sleep(0.5)
    while True:
        screen.blit(bg, (0,0))
        screen.blit(titletext, (GetCenter(width,height,titletext)[0], GetCenter(width, height, titletext)[1] - 155))
        screen.blit(twoplayer, (GetCenter(width,height,twoplayer)[0],GetCenter(width,height,twoplayer)[1] - 55))
        screen.blit(threeplayer,(GetCenter(width,height,threeplayer)[0],GetCenter(width,height,threeplayer)[1] + 55))
        screen.blit(fourplayer,(GetCenter(width,height,fourplayer)[0],GetCenter(width,height,fourplayer)[1] + 165))
           
        pygame.event.get()
 
       
        if twoplayer.get_rect(topleft=(GetCenter(width,height,twoplayer)[0],GetCenter(width,height,twoplayer)[1] - 55)).collidepoint(pygame.mouse.get_pos()):
            screen.blit(twoplayerh,(GetCenter(width,height,twoplayer)[0],GetCenter(width,height,twoplayer)[1] - 55))
        if threeplayer.get_rect(topleft=(GetCenter(width,height,threeplayer)[0],GetCenter(width,height,threeplayer)[1] + 55)).collidepoint(pygame.mouse.get_pos()):
            screen.blit(threeplayerh,(GetCenter(width,height,threeplayer)[0],GetCenter(width,height,threeplayer)[1] + 55))
        if fourplayer.get_rect(topleft=(GetCenter(width,height,fourplayer)[0],GetCenter(width,height,fourplayer)[1] + 165)).collidepoint(pygame.mouse.get_pos()):
            screen.blit(fourplayerh,(GetCenter(width,height,fourplayer)[0],GetCenter(width,height,fourplayer)[1] + 165))
        if (pygame.mouse.get_pressed()==(1,0,0)) and twoplayer.get_rect(topleft=(GetCenter(width,height,twoplayer)[0],GetCenter(width,height,twoplayer)[1] - 55)).collidepoint(pygame.mouse.get_pos()):
            return 2
        if (pygame.mouse.get_pressed()==(1,0,0)) and threeplayer.get_rect(topleft=(GetCenter(width,height,threeplayer)[0],GetCenter(width,height,threeplayer)[1] + 55)).collidepoint(pygame.mouse.get_pos()):
            return 3
        if (pygame.mouse.get_pressed()==(1,0,0)) and fourplayer.get_rect(topleft=(GetCenter(width,height,fourplayer)[0],GetCenter(width,height,fourplayer)[1] + 165)).collidepoint(pygame.mouse.get_pos()):
            return 4
        pygame.display.update()