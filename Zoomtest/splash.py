import pygame
import time
from Getcenter import *

black = (0,0,0)
white = (255,255,255)

def SplashScreen(screen,width,height):
  screen.fill(white)
  templogo = pygame.image.load("content\\logo.png").convert()
  tempglove = pygame.image.load("content\\glove.png").convert()
  tempvar = 0
  templogo.set_alpha(tempvar)
  pos = GetCenter(width,height,templogo)
  glovepos = GetCenter(width,height,tempglove)
  tempimage = pygame.transform.scale(pygame.image.load("content\\Board3d.png").convert(), (width,height))
  while not tempvar >= 150:
    screen.blit(templogo, pos)
    tempvar += 4
    templogo.set_alpha(tempvar)
    pygame.display.flip()
    time.sleep(0.033)
  tempvar = 0
  time.sleep(1)
  offColorSq = pygame.Surface((width,height), pygame.SRCALPHA, 32)
  while not tempvar >= 150:
    tempvar += 6
    offColorSq.fill((0,0,0, tempvar))
    screen.blit(offColorSq, (0,0))
    pygame.display.flip()
    time.sleep(0.033)
  screen.fill(black)
  tempvar = 0
  tempglove.set_alpha(tempvar)
  while not tempvar >= 150:
    screen.blit(tempglove, (glovepos[0], glovepos[1] - (height / 6)))
    tempvar += 4
    tempglove.set_alpha(tempvar)
    pygame.display.flip()
    time.sleep(0.033)
  tempvar = 0
  time.sleep(1)
  tempimage.set_alpha(tempvar)
  while not tempvar >= 250:
    screen.blit(tempimage, (0,0))
    screen.blit(pygame.image.load("content\\glove.png").convert_alpha(), (glovepos[0], glovepos[1] - (height / 6)))
    tempvar += 10
    tempimage.set_alpha(tempvar)
    pygame.display.flip()
    time.sleep(0.033)