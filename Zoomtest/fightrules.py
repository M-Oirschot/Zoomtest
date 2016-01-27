import pygame

def superfight(player, fight):
    playerdmg = fight[0]
    playercond = fight[1]
    sdmg = fight[2]

    if sdmg > playerdmg:
        sdmg -= playerdmg
        player.Lifepoints -= sdmg
        player.Conditionpoints -= playercond
    else:
        player.Conditionpoints -= playercond

def pvp():
    playeronedmg = fight[0]
    playeronecond = fight[1]
    playertwodmg = fight[2]
    playertwocond = fight[3]
    
    if playeronedmg > playertwodmg:
        playeronedmg -= playertwodmg
        playertwo.Lifepoints -= playeronedmg 
        
        playerone.Conditionpoints -= playeronecond
        playertwo.Conditionpoints -= playertwocond

