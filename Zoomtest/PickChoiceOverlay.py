import pygame
from Getcenter import *

def PlayerversusPlayer(screen,width,height):
  maincolor = (20,66,112)

  square = pygame.Surface((421,421), pygame.SRCALPHA, 32)
  square.fill(maincolor)
  screen.blit(square, (GetCenter(width,height,square)[0] + (width / 6), GetCenter(width,height,square)[1]))
  pygame.display.flip()