import pygame

def superfight(player, fight):
    playerdmg = fight[0]
    playercond = fight[1]
    sdmg = fight[2]         #dmg of the Superfighter

    if sdmg > playerdmg:
        sdmg -= playerdmg
        player.Lifepoints -= sdmg
        player.Conditionpoints -= playercond
    else:
        player.Conditionpoints -= playercond

def pvp(attacker,defender,fight):
    playeronedmg = fight[0]     #playerone is attacker
    playeronecond = fight[1]    #playertwo is defender
    playertwodmg = fight[2]
    playertwocond = fight[3]
    
    if playeronedmg > playertwodmg:
        playeronedmg -= playertwodmg
        defender.Lifepoints -= playeronedmg 
        
        attacker.Conditionpoints -= playeronecond
        defender.Conditionpoints -= playertwocond
    elif playertwodmg > playeronedmg:
        playertwodmg -= playeronedmg
        attacker.Lifepoints -= playertwodmg

        attacker.Conditionpoints -= playeronecond
        defender.Conditionpoints -= playertwocond
    else:
        attacker.Conditionpoints -= playeronecond
        defender.Conditionpoints -= playertwocond
   
def AliveCheck(players):
    alive = 0
    for i in range (0,len(players)):
        if players[i] != 0:
            alive += 1
    return alive

def removeDead(players):
    newlist = []
    for i in range(len(players)):
        if not players[i].health <= 0:
            newlist += [player[i]]
    return newlist

def removeTile(Stile, dead):
    newlist = []
    for i in range(Stile):
        if not Stile[i] == dead:
            newlist += [player[i]]
    return newlist


            







