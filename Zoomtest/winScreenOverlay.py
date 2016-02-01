import pygame
from Getcenter import *

def winScreen(screen, width, height, winner):
    font = pygame.font.Font("content\\font\\retro.ttf", 30)
    square = pygame.image.load("content\\eventscreen.png")
    wPlayer = font.render("Player: " + winner + " wins!", 1, (255,0,0))
    
    screen.blit(square, (GetCenter(width,height,square)))
    screen.blit(wPlayer, (GetCenter(width, height, wPlayer)[0], GetCenter(width,height, wPlayer)[1] - (height / 3.3)))
