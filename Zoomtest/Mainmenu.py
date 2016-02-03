from Getcenter import *
import pygame
import time
from PickChoiceOverlay import *

black = (0,0,0)
white = (255,255,255)

 
def mainMenu(screen,width, height, mute):
    
    pygame.mixer.music.load("content\\sound\\EoT.mid")
    if mute == False:
        pygame.mixer.music.play(-1,0.0)
    font = pygame.font.Font(None, 40)
    img = pygame.transform.scale(pygame.image.load("content\\Board3d.png").convert(), (width,height))
    realglove = pygame.image.load("content\\title.png").convert_alpha()
    textButton1 = pygame.image.load('content\start.png')
    textButton1h = pygame.image.load('content\start_h.png')
    textButton2 = pygame.image.load('content\\settings.png')
    textButton2h = pygame.image.load('content\settingsh.png')
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


def settingScreen(mute,screen,width,height):
    font = pygame.font.Font("content\\font\\retro.ttf", 75)
    smallfont = pygame.font.Font("content\\font\\retro.ttf", 30)
    square = pygame.image.load("content\\eventscreen.png")
    back = pygame.image.load("content\\back.png" )
    back_h = pygame.image.load("content\\back_h.png")
    soundT = pygame.transform.scale(pygame.image.load("content\\sound.png"), (175,50))
    soundT_h = pygame.transform.scale(pygame.image.load("content\\sound_h.png"), (175,50))

    screen.blit(square, GetCenter(width,height,square))
    settingsText = font.render("Settings", 1, (0,0,0))
    screen.blit(settingsText, (GetCenter(width,height,settingsText)[0], GetCenter(width,height,settingsText)[1] - (height / 3) + 35))
    while True:
        screen.blit(soundT, (GetCenter(width,height,soundT)[0],GetCenter(width,height,soundT)[1]+ (height / 6)))
        screen.blit(back, (GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6) + 70))
        pygame.event.get()

        if soundT.get_rect(topleft=(GetCenter(width,height,soundT)[0],GetCenter(width,height,soundT)[1]+ (height / 6))).collidepoint(pygame.mouse.get_pos()):
            screen.blit(soundT_h,(GetCenter(width,height,soundT)[0],GetCenter(width,height,soundT)[1]+ (height / 6)))
        if (pygame.mouse.get_pressed()==(1,0,0) and soundT.get_rect(topleft=(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6))).collidepoint(pygame.mouse.get_pos())):
            if mute == False:
                mute = True
                pygame.mixer.music.fadeout(1000)
                smallrect = pygame.Surface((300,70), pygame.SRCALPHA, 32)
                soundTextMeme = smallfont.render("Sound is off" , 1, (0,0,0))
                smallrect.fill((150,150,150))
                screen.blit(smallrect, (GetCenter(width,height,smallrect)[0],GetCenter(width,height,smallrect)[1] + (height / 6) - 70))
                screen.blit(soundTextMeme, (GetCenter(width,height,soundTextMeme)[0],GetCenter(width,height,soundTextMeme)[1] + (height / 6) - 70))
                pygame.display.flip()
                time.sleep(0.5)
            else:
                mute = False
                smallrect = pygame.Surface((300,70), pygame.SRCALPHA, 32)
                soundTextMeme = smallfont.render("Sound is on" , 1, (0,0,0))
                smallrect.fill((150,150,150))
                screen.blit(smallrect, (GetCenter(width,height,smallrect)[0],GetCenter(width,height,smallrect)[1] + (height / 6) - 70))
                screen.blit(soundTextMeme, (GetCenter(width,height,soundTextMeme)[0],GetCenter(width,height,soundTextMeme)[1] + (height / 6) - 70))
                pygame.display.flip()
                time.sleep(0.5)                

        if back.get_rect(topleft=(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6) + 70)).collidepoint(pygame.mouse.get_pos()):
            screen.blit(back_h,(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6) + 70))
        if (pygame.mouse.get_pressed()==(1,0,0) and back.get_rect(topleft=(GetCenter(width,height,back)[0],GetCenter(width,height,back)[1]+ (height / 6) + 70)).collidepoint(pygame.mouse.get_pos())):
            return mute
        pygame.display.flip()
