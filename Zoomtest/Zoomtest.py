﻿import pygame
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
from PickChoiceOverlay import *
from Player import *
#dankmemes
preset = 1

pone = pygame.image.load("content\\player1pion.png")
ptwo = pygame.image.load("content\\player2pion.png")
pthree = pygame.image.load("content\\player3pion.png")
pfour = pygame.image.load("content\\player4pion.png")

if preset == 0:
  width = 800 #int(input("Width: " ))
  height = 600 #int(input("Height: "))
  size = (width,height)
  screen = pygame.display.set_mode(size)
if preset == 1:
  width = 1920  
  height = 1080
  size = (width,height)
  #screen = pygame.display.set_mode(size)
  screen = pygame.display.set_mode((size),pygame.FULLSCREEN)
while True:
  if width >= 800 and height >= 600:
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
    playercount = Playerselect(screen,width,height)      
    for i in range (0,playercount):
      list = Node("", list)
    namelist = name(list,screen,width,height)
    emptyList = Empty
    if playercount == 2:
      emptyList = Node(MakePlayer(0,100,15,ptwo,namelist.Value,2),emptyList)
      emptyList = Node(MakePlayer(10,100,15,pone,namelist.Tail.Value,1),emptyList)
      
      
    elif playercount == 3:
      emptyList = Node(MakePlayer(0,100,15,pthree,namelist.Value,3),emptyList)
      emptyList = Node(MakePlayer(10,100,15,ptwo,namelist.Tail.Value,2),emptyList)
      emptyList = Node(MakePlayer(20,100,15,pone,namelist.Tail.Tail.Value,1),emptyList)
    elif playercount == 4:
      emptyList = Node(MakePlayer(0,100,15,pfour,namelist.Value,4),emptyList)
      emptyList = Node(MakePlayer(10,100,15,pthree,namelist.Tail.Value,3),emptyList)
      emptyList = Node(MakePlayer(20,100,15,ptwo,namelist.Tail.Tail.Value,2),emptyList)
      emptyList = Node(MakePlayer(30,100,15,pone,namelist.Tail.Tail.Tail.Value,1),emptyList)
    clearPygame(white)
    coolstorage = PlayerversusPlayer(screen,width,height,MakePlayer(0,100,15,1,namelist.Value,1),MakePlayer(10,100,15,1,namelist.Tail.Value,2))
    #Main(screen,width,height,playercount,emptyList)
    
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

#player1 = MakePlayer(0,0,100,15,3,"Bamischijf",1)
#print(player1.dmg.five.one.dmg)
#print(player1.Name)
#print(player1.dmg.six.three.cond)

