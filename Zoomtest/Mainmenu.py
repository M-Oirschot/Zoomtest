from Getcenter import *
import pygame
import time
from PickChoiceOverlay import *
black = (0,0,0)
white = (255,255,255)
 
def mainMenu(screen,width, height):
  pygame.mixer.music.load("content\\sound\\main.mp3")
  pygame.mixer.music.play(-1,0.0)
  font = pygame.font.Font(None, 40)
  img = pygame.transform.scale(pygame.image.load("content\\Board3d.png").convert(), (width,height))
  realglove = pygame.image.load("content\\glove.png").convert_alpha()
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
    screen.blit(pygame.image.load("content\\glove.png").convert_alpha(), (GetCenter(width,height,realglove)[0], GetCenter(width,height,realglove)[1] - (height / 6)))
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