from Getcenter import *
import pygame
import time

black = (0,0,0)
white = (255,255,255)

def mainMenu(screen,width, height):	
  font = pygame.font.Font(None, 40)
  img = pygame.transform.scale(pygame.image.load("content\\Board3d.png").convert(), (width,height))
  realglove = pygame.image.load("content\\glove.png").convert_alpha()
  textButton1 = font.render("Start game", 1, black)
  textButton2 = font.render("Highscores", 1, black)
  textButton3 = font.render("Rules", 1, black)
  textButton4 = font.render("Quit", 1, black)  
  button1 = pygame.Surface((175,50), pygame.SRCALPHA, 32)
  memes = 0
  while True:
    screen.blit(img, (0,0))
    screen.blit(pygame.image.load("content\\glove.png").convert_alpha(), (GetCenter(width,height,realglove)[0], GetCenter(width,height,realglove)[1] - (height / 6)))
    button1.fill((100,100,100))
    screen.blit(button1, (GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8 - 10)))
    screen.blit(textButton1, (GetCenter(width,height,textButton1)[0], GetCenter(width,height,textButton1)[1] + (height / 8) - 10))
    screen.blit(button1, (GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8 + 45)))
    screen.blit(textButton2, (GetCenter(width,height,textButton2)[0], GetCenter(width,height,textButton2)[1] + (height / 8) + 45))
    screen.blit(button1, (GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8 + 100)))
    screen.blit(textButton3, (GetCenter(width,height,textButton3)[0], GetCenter(width,height,textButton3)[1] + (height / 8) + 100))
    screen.blit(button1, (GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8 + 155)))
    screen.blit(textButton4, (GetCenter(width,height,textButton4)[0], GetCenter(width,height,textButton3)[1] + (height / 8) + 155))
    pygame.event.get()
    #Start Game
    if (pygame.mouse.get_pressed()==(1,0,0)  and button1.get_rect(topleft=(GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8 - 10))).collidepoint(pygame.mouse.get_pos())):
      return 1
    if (pygame.mouse.get_pressed()==(1,0,0)  and button1.get_rect(topleft=(GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8) + 45)).collidepoint(pygame.mouse.get_pos())):
      return 2
    if (pygame.mouse.get_pressed()==(1,0,0)  and button1.get_rect(topleft=(GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8) + 100)).collidepoint(pygame.mouse.get_pos())):
      return 3
    if (pygame.mouse.get_pressed()==(1,0,0)  and button1.get_rect(topleft=(GetCenter(width,height,button1)[0], GetCenter(width,height,button1)[1] + (height / 8) + 155)).collidepoint(pygame.mouse.get_pos())):
      return 4
    pygame.display.flip()
    time.sleep(0.033)