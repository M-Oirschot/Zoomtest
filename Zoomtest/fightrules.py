import pygame

def fight(playerOne, playerTwo):
    firstdice = dice(6)
    seconddice = dice(6)
    if seconddice == 1:
        playerOne.dmg.