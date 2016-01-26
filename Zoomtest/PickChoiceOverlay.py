import pygame
from Getcenter import *

def PlayerversusPlayer(screen,width,height,player1,player2):
  maincolor = (100,100,100)

  square = pygame.Surface((width - 200,height - 200), pygame.SRCALPHA, 32)
  outline = pygame.Surface((width - 190, height - 190), pygame.SRCALPHA, 32)
  square.fill(maincolor)
  outline.fill((0,0,0))
  screen.blit(outline, (GetCenter(width,height,outline)))
  screen.blit(square, (GetCenter(width,height,square)))
  pygame.display.flip()

def PlayerversusSuperfight(screen,width,height,player1,fighterlist):
  maincolor = (100,100,100)

  square = pygame.Surface((width - 200,height - 200), pygame.SRCALPHA, 32)
  outline = pygame.Surface((width - 190, height - 190), pygame.SRCALPHA, 32)
  square.fill(maincolor)
  outline.fill((0,0,0))
  screen.blit(outline, (GetCenter(width,height,outline)))
  screen.blit(square, (GetCenter(width,height,square)))
  pygame.display.flip()