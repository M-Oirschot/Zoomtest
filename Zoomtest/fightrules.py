import pygame

def superfight(player, fight):
    playerdmg = fight[0]
    playercond = fight[1]
    sdmg = fight[2]

    if sdmg > playerdmg:
        sdmg -= playerdmg
        player.Lifepoints -= sdmg
        player.conditionpoints -= playercond
