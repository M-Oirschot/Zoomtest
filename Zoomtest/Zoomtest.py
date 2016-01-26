import pygame
import time
import os
from splash import *
from Getcenter import *
from Mainmenu import *
from entername_here import *
from Node import *
from Basegame import *
from Player import *
from Selectplayers import *
from resolution_switch import *
from GetRandomEvent import *
from Player import *
#dankmemes
preset = 1
if preset == 0:
  width = 1000#int(input("Width: " ))
  height = 800#int(input("Height: "))
  size = (width,height)
  screen = pygame.display.set_mode(size)
if preset == 1:
  width = 1920
  height = 1080
  size = (width,height)
  screen = pygame.display.set_mode((size),pygame.FULLSCREEN)
while True:
  if width >= 800 and width and height >= 600:
    break
  else:
    print("Resolution must be at least 800x600")
    input("Press enter to continue...")
    os.system('cls')

def clearPygame(color):
  screen.fill(color)
  pygame.display.flip()

pygame.init()
size=(width,height)

black = (0,0,0)
white = (255,255,255)

#Main File

SplashScreen(screen,width,height)
#"""
while True:
  pressed = mainMenu(screen,width,height)
  if pressed == 1:
    list = Empty      
    playercount = Playerselect(screen,width,height)                
    for i in range (0,playercount):
      list = Node("", list)
    nameslist = name(list,screen,width,height)# Put players into list as soon as we work out coordinates
        
    clearPygame(white)
    Main(screen,width,height,nameslist,playercount)
    
  elif pressed == 4:
    pygame.quit()
    break
  elif pressed == 2:
    print("Highscores go here")           #Hier komt de highscore function
  elif pressed == 3:
    print("Help goes here")               #Hier komt de help/rules function
#"""
#while True:
#pygame.display.flip()
#  time.sleep(0.1)
#print(glove.get_rect().size)


