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
preset = 0
if preset == 0:
  width = 800 #int(input("Width: " ))
  height = 600 #int(input("Height: "))
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

#SplashScreen(screen,width,height)
while True:
  pressed = mainMenu(screen,width,height)
  if pressed == 1:
    list = Empty                      
    for i in range (0,Playerselect(screen,width,height)):
      list = Node("", list)
    name(list,screen,width,height)
    clearPygame(white)
    Main(screen,width,height)
    
  elif pressed == 4:
    pygame.quit()
    break
  elif pressed == 2:
    print("Highscores go here")           #Hier komt de highscore function
  elif pressed == 3:
    print("Help goes here")               #Hier komt de help/rules function
#while True:
#pygame.display.flip()
#  time.sleep(0.1)
#print(glove.get_rect().size)

player1 = MakePlayer(0,0,100,15,3,"Bamischijf",1)
print(player1.dmg.five.one.dmg)
print(player1.Name)
print(player1.dmg.six.three.cond)

