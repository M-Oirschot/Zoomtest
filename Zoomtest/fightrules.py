import pygame

def superfight(player):
    #if player pos = superfight tile
    fight = PlayerversusSuperfight(screen, width, height, player[1], fighterlist)
    playerdmg = fight[0]
    playercond = fight[1]
    sdmg = fight[2]