import pygame
from Getcenter import *

def winScreen(screen, width, height, winner):
    textButton4 = pygame.image.load('content\quit.png')
    textButton4h = pygame.image.load('content\quit_h.png')
    font = pygame.font.Font("content\\font\\retro.ttf", 30)
    square = pygame.image.load("content\\eventscreen.png")
    wPlayer = font.render("Player: " + winner + " wins!", 1, (255,0,0))
    
    screen.blit(square, (GetCenter(width,height,square)))
    screen.blit(wPlayer, (GetCenter(width, height, wPlayer)[0], GetCenter(width,height, wPlayer)[1] - (height / 3.3)))
    screen.blit(textButton4, (GetCenter(width,height,textButton4)))
    
    while True:
        screen.blit(textButton4, (GetCenter(width,height,textButton4)))
        pygame.event.get()
        if textButton4.get_rect(topleft=(GetCenter(width,height,textButton4))).collidepoint(pygame.mouse.get_pos()):
            screen.blit(textButton4h,(GetCenter(width,height,textButton4)))

        if (pygame.mouse.get_pressed()==(1,0,0)  and textButton4.get_rect(topleft=(GetCenter(width,height,textButton4))).collidepoint(pygame.mouse.get_pos())):
                return
        pygame.display.flip()