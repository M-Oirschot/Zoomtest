from Getcenter import *
import pygame
import time
from PickChoiceOverlay import *

black = (0,0,0)
white = (255,255,255)
mute = False
 
def mainMenu(screen,width, height):
    pygame.mixer.music.load("content\\sound\\EoT.mid")
    pygame.mixer.music.play(-1,0.0)
    font = pygame.font.Font(None, 40)
    img = pygame.transform.scale(pygame.image.load("content\\Board3d.png").convert(), (width,height))
    realglove = pygame.image.load("content\\title.png").convert_alpha()
    textButton1 = pygame.image.load('content\start.png')
    textButton1h = pygame.image.load('content\start_h.png')
    textButton2 = pygame.image.load('content\highscores.png')
    textButton2h = pygame.image.load('content\highscores_h.png')
    textButton3 = pygame.image.load('content\\rules.png')
    textButton3h = pygame.image.load('content\\rules_h.png')
    textButton4 = pygame.image.load('content\quit.png')
    textButton4h = pygame.image.load('content\quit_h.png')
 
    memes = 0
    while True:
        screen.blit(img, (0,0))
        screen.blit(realglove, (GetCenter(width,height,realglove)[0], GetCenter(width,height,realglove)[1] - (height / 6)))
        screen.blit(textButton1, (GetCenter(width,height,textButton1)[0], GetCenter(width,height,textButton1)[1] + (height / 8) - 10))
        screen.blit(textButton2, (GetCenter(width,height,textButton2)[0], GetCenter(width,height,textButton2)[1] + (height / 8) + 45))
        screen.blit(textButton3, (GetCenter(width,height,textButton3)[0], GetCenter(width,height,textButton3)[1] + (height / 8) + 100))
        screen.blit(textButton4, (GetCenter(width,height,textButton4)[0], GetCenter(width,height,textButton4)[1] + (height / 8) + 155))

        if textButton1.get_rect(topleft=(GetCenter(width,height,textButton1)[0],GetCenter(width,height,textButton1)[1] + (height / 8 - 10))).collidepoint(pygame.mouse.get_pos()):
                screen.blit(textButton1h,(GetCenter(width,height,textButton1)[0],GetCenter(width,height,textButton1)[1] + (height / 8 - 10)))
        if textButton2.get_rect(topleft=(GetCenter(width,height,textButton2)[0],GetCenter(width,height,textButton2)[1] + (height / 8 + 45))).collidepoint(pygame.mouse.get_pos()):
                screen.blit(textButton2h,(GetCenter(width,height,textButton2)[0],GetCenter(width,height,textButton2)[1] + (height / 8 + 45)))
        if textButton3.get_rect(topleft=(GetCenter(width,height,textButton3)[0],GetCenter(width,height,textButton3)[1] + (height / 8 + 100))).collidepoint(pygame.mouse.get_pos()):
                screen.blit(textButton3h,(GetCenter(width,height,textButton3)[0],GetCenter(width,height,textButton3)[1] + (height / 8 + 100)))
        if textButton4.get_rect(topleft=(GetCenter(width,height,textButton4)[0],GetCenter(width,height,textButton4)[1] + (height / 8 + 155))).collidepoint(pygame.mouse.get_pos()):
                screen.blit(textButton4h,(GetCenter(width,height,textButton4)[0],GetCenter(width,height,textButton4)[1] + (height / 8 + 155)))
 
        pygame.event.get()
        #Start Game
        if (pygame.mouse.get_pressed()==(1,0,0)  and textButton1.get_rect(topleft=(GetCenter(width,height,textButton1)[0], GetCenter(width,height,textButton1)[1] + (height / 8 - 10))).collidepoint(pygame.mouse.get_pos())):
            return 1
        if (pygame.mouse.get_pressed()==(1,0,0)  and textButton1.get_rect(topleft=(GetCenter(width,height,textButton1)[0], GetCenter(width,height,textButton1)[1] + (height / 8) + 45)).collidepoint(pygame.mouse.get_pos())):
            return 2
        if (pygame.mouse.get_pressed()==(1,0,0)  and textButton1.get_rect(topleft=(GetCenter(width,height,textButton1)[0], GetCenter(width,height,textButton1)[1] + (height / 8) + 100)).collidepoint(pygame.mouse.get_pos())):
            return 3
        if (pygame.mouse.get_pressed()==(1,0,0)  and textButton1.get_rect(topleft=(GetCenter(width,height,textButton1)[0], GetCenter(width,height,textButton1)[1] + (height / 8) + 155)).collidepoint(pygame.mouse.get_pos())):
            return 4
        pygame.display.flip()
        time.sleep(0.033)


def settingScreen(mute):
    font = pygame.font.Font("content\\font\\retro.ttf", 75)
    square = pygame.image.load("content\\eventscreen.png")
    back = pygame.image.load("content\\back.png" )
    back_h = pygame.image.load("content\\back_h.png")
    soundT = pygame.imgage.load("")
    soundT_h = pygame.image.load("")

    screen.blit(square, GetCenter(width,height,square))
    settingsText = font.render("Settings", 1, (0,0,0))
    screen.blit(settingText, (GetCenter(width,height,settingsText)[0], GetCenter(width,height,settingsText)[1] - (height / 3) + 35))
    while True:
        screen.blit(soundT, (GetCenter(width,height,soundT)[0],GetCenter(width,height,soundT)[1]+ (height / 6)))
        screen.blit(back, (GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6)))
        screen.blit(quit, (GetCenter(width,height,back)[0],GetCenter(width,height,back)[1] +(height / 6) + 70))
        pygame.event.get()

        if soundT.get_rect(topleft=(GetCenter(width,height,soundT)[0],GetCenter(width,height,soundT)[1]+ (height / 6))).collidepoint(pygame.mouse.get_pos()):
            screen.blit(soundT_h,(GetCenter(width,height,soundT)[0],GetCenter(width,height,soundT)[1]+ (height / 6)))
        if (pygame.mouse.get_pressed()==(1,0,0) and soundT.get_rect(topleft=(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6))).collidepoint(pygame.mouse.get_pos())):
            if mute == False:
                mute = True
            else:
                mute = False

        if back.get_rect(topleft=(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6))).collidepoint(pygame.mouse.get_pos()):
            screen.blit(back_h,(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6)))
        if (pygame.mouse.get_pressed()==(1,0,0) and back.get_rect(topleft=(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6))).collidepoint(pygame.mouse.get_pos())):
            return 
        pygame.display.flip()
