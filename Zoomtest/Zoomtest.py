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
from PickChoiceOverlay import *
from Player import *
#dankmemes
preset = 1

pone = pygame.image.load("content\\player4pion.png")
ptwo = pygame.image.load("content\\player3pion.png")
pthree = pygame.image.load("content\\player2pion.png")
pfour = pygame.image.load("content\\player1pion.png")

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

   

asdf = build_square_board(11,5)
tpboard = Empty
while not asdf.IsEmpty:
    tpboard = Node(asdf.Value, tpboard)
    asdf = asdf.Tail

pygame.init()
size=(width,height)

black = (0,0,0)
white = (255,255,255)

#Main File
pygame.mixer.music.load("content\\sound\\vape.mp3")
pygame.mixer.music.play(-1,0.0)

SplashScreen(screen,width,height)

pygame.mixer.music.fadeout(1000)
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
            emptyList = Node(MakePlayer(0,80,15,pfour,namelist.Tail.Value,2,tpboard.Value),emptyList)
            emptyList = Node(MakePlayer(20,80,15,ptwo,namelist.Value,1,getItemFromList(tpboard,20,0)),emptyList)
            flippedList = Node(emptyList.Tail.Value, Node(emptyList.Value, Empty))
        elif playercount == 3:
            emptyList = Node(MakePlayer(0,90,15,pfour,namelist.Tail.Tail.Value,3, tpboard.Value),emptyList)
            emptyList = Node(MakePlayer(20,90,15,ptwo,namelist.Tail.Value,1, getItemFromList(tpboard,20,0)),emptyList)
            emptyList = Node(MakePlayer(10,90,15,pthree,namelist.Value,2, getItemFromList(tpboard,10,0)),emptyList)
            flippedList = Node(emptyList.Tail.Tail.Value, Node(emptyList.Tail.Value, Node(emptyList.Value, Empty)))
        elif playercount == 4:
            emptyList = Node(MakePlayer(0,100,15,pfour,namelist.Tail.Tail.Tail.Value,4, tpboard.Value),emptyList)
            emptyList = Node(MakePlayer(10,100,15,pthree,namelist.Tail.Value,3, getItemFromList(tpboard,10,0)),emptyList)
            emptyList = Node(MakePlayer(20,100,15,ptwo,namelist.Tail.Tail.Value,2, getItemFromList(tpboard,20,0)),emptyList)
            emptyList = Node(MakePlayer(30,100,15,pone,namelist.Value,1, getItemFromList(tpboard,30,0)),emptyList)
            flippedList = Node(emptyList.Tail.Tail.Tail.Value, Node(emptyList.Tail.Value, Node(emptyList.Tail.Tail.Value, Node(emptyList.Value, Empty))))
        Main(screen,width,height,playercount,flippedList,tpboard)
    
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

