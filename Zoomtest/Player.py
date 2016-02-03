import random 
from PickChoiceOverlay import *
class Player:
    def __init__(self,starting, lifepoints, conditionpoints, texture, name, tile, dmg):
        self.Starting = starting
        self.Lifepoints = lifepoints
        self.Conditionpoints = conditionpoints
        self.Texture = texture
        self.Name = name
        self.dmg = dmg
        self.Pos = starting
        self.Tile = tile

class dmgList:
    def __init__(self, one, two, three):
        self.one = one
        self.two = two
        self.three = three

class dmgItem:
    def __init__(self, dmg, cond):
        self.dmg = dmg
        self.cond = cond

class dmg:
    def __init__(self, one, two, three, four, five, six):
        self.one = one
        self.two = two
        self.three = three
        self.four = four
        self.five = five
        self.six = six

def MakePlayer(x,health,condition,texture,name,playernum,tile):
  if playernum == 1:
    return Player(x,health,condition,texture,name, tile,dmg(dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)), 
                                                    dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15, 5)), 
                                                    dmgList(dmgItem(7, 2), dmgItem(12, 3), dmgItem(16, 4)),
                                                    dmgList(dmgItem(2, 1), dmgItem(2, 1), dmgItem(6, 3)),
                                                    dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8)),
                                                    dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5))))
  if playernum  == 2:
    return Player(x,health,condition,texture,name, tile,dmg(dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15, 5)), 
                                                    dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)), 
                                                    dmgList(dmgItem(2, 1), dmgItem(4, 2), dmgItem(6, 4)),
                                                    dmgList(dmgItem(7, 2), dmgItem(12, 3), dmgItem(16, 4)),
                                                    dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5)),
                                                    dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8))))
  if playernum == 3:
    return Player(x,health,condition,texture,name, tile,dmg(dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8)), 
                                                    dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5)), 
                                                    dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)),
                                                    dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15,5)),
                                                    dmgList(dmgItem(7, 2), dmgItem(12, 3), dmgItem(16, 4)),
                                                    dmgList(dmgItem(2, 1), dmgItem(4, 2), dmgItem(6, 3))))
  if playernum == 4:
    return Player(x,health,condition,texture,name, tile,dmg(dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5)), 
                                                    dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8)), 
                                                    dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15, 5)),
                                                    dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)),
                                                    dmgList(dmgItem(2, 1), dmgItem(4, 2), dmgItem(6, 3)),
                                                    dmgList(dmgItem(7, 2), dmgItem(12, 3), dmgItem(16, 4))))


def checkPlayers(playerlist):
    if len(playerlist) == 2:
        if playerlist[0].Tile.pos == playerlist[1].Tile.pos:
            return [playerlist[0], playerlist[1]]
        else:
            return []
    elif len(playerlist) == 3:
        if playerlist[0].Tile.pos == playerlist[1].Tile.pos and playerlist[1].Tile.pos == playerlist[2].Tile.pos:
            return [playerlist[0], playerlist[1], playerlist[2]]
        elif playerlist[0].Tile.pos == playerlist[1].Tile.pos:
            return [playerlist[0], playerlist[1]]
        elif playerlist[1].Tile.pos == playerlist[2].Tile.pos:
            return [playerlist[1], playerlist[2]]
        elif playerlist[0].Tile.pos == playerlist[2].Tile.pos:
            return[playerlist[0],playerlist[2]]
        else:
            return []
    elif len(playerlist) == 4:
        if playerlist[0].Tile.pos == playerlist[1].Tile.pos and playerlist[1].Tile.pos == playerlist[2].Tile.pos and playerlist[2].Tile.pos == playerlist[3].Tile.pos:
            return [playerlist[0], playerlist[1], playerlist[2], playerlist[3]]
        elif playerlist[0].Tile.pos == playerlist[1].Tile.pos and playerlist[1].Tile.pos == playerlist[2].Tile.pos:
            return [playerlist[0], playerlist[1], playerlist[2]]
        elif playerlist[1].Tile.pos == playerlist[2].Tile.pos and playerlist[1].Tile.pos == playerlist[3].Tile.pos:
            return [playerlist[1], playerlist[2], playerlist[3]]
        elif playerlist[0].Tile.pos == playerlist[1].Tile.pos and playerlist[1].Tile.pos == playerlist[3].Tile.pos:
            return [playerlist[0], playerlist[1], playerlist[3]]
        elif playerlist[0].Tile.pos == playerlist[2].Tile.pos and playerlist[3].Tile.pos == playerlist[2].Tile.pos:
            return [playerlist[0], playerlist[2], playerlist[3]]
        elif playerlist[0].Tile.pos == playerlist[2].Tile.pos:  
            return [playerlist[0], playerlist[2]]
        elif playerlist[0].Tile.pos == playerlist[3].Tile.pos:
            return [playerlist[0], playerlist[3]]
        elif playerlist[2].Tile.pos == playerlist[3].Tile.pos:
            return [playerlist[2], playerlist[3]]
        elif playerlist[1].Tile.pos == playerlist[3].Tile.pos:
            return [playerlist[1], playerlist[3]]
        elif playerlist[0].Tile.pos == playerlist[1].Tile.pos:
            return [playerlist[0], playerlist[1]]
        elif playerlist[1].Tile.pos == playerlist[2].Tile.pos:
            return [playerlist[1], playerlist[2]]
        else:
            return []

def checkPvp(playerlist,screen,width,height):
    bg = pygame.transform.scale(pygame.image.load("content\\board.png"), (width,height))
    if len(playerlist) == 2:
        if playerlist[0].Tile.pos == playerlist[1].Tile.pos:
            UltraPVP(screen,width,height,playerlist[0],playerlist[1])
            screen.blit(bg, (0,0))
    elif len(playerlist) == 3:
        if playerlist[0].Tile.pos == playerlist[1].Tile.pos:
            UltraPVP(screen,width,height,playerlist[0],playerlist[1])
            screen.blit(bg, (0,0))
        if playerlist[1].Tile.pos == playerlist[2].Tile.pos:
            UltraPVP(screen,width,height,playerlist[1],playerlist[2])
            screen.blit(bg, (0,0))
        if playerlist[0].Tile.pos == playerlist[2].Tile.pos:
            UltraPVP(screen,width,height,playerlist[0],playerlist[2])
            screen.blit(bg, (0,0))
    elif len(playerlist) == 4:
        if playerlist[0].Tile.pos == playerlist[2].Tile.pos:
            UltraPVP(screen,width,height,playerlist[0],playerlist[2])
            screen.blit(bg, (0,0))
        if playerlist[0].Tile.pos == playerlist[3].Tile.pos:
            UltraPVP(screen,width,height,playerlist[0],playerlist[3])
            screen.blit(bg, (0,0))
        if playerlist[2].Tile.pos == playerlist[3].Tile.pos:
            UltraPVP(screen,width,height,playerlist[2],playerlist[3])
            screen.blit(bg, (0,0))
        if playerlist[1].Tile.pos == playerlist[3].Tile.pos:
            UltraPVP(screen,width,height,playerlist[1],playerlist[3])
            screen.blit(bg, (0,0))
        if playerlist[0].Tile.pos == playerlist[1].Tile.pos:
            UltraPVP(screen,width,height,playerlist[0],playerlist[1])
            screen.blit(bg, (0,0))
        if playerlist[1].Tile.pos == playerlist[2].Tile.pos:
            UltraPVP(screen,width,height,playerlist[1],playerlist[2])
            screen.blit(bg, (0,0))

def printVisuals(player, screen, width, height):
    statfont = pygame.font.Font("content\\font\\retro.ttf", 25)
    player1health = statfont.render("Health: " + str(player[0].Lifepoints), 1, (0,0,0))
    player1stamina = statfont.render("Stamina: " + str(player[0].Conditionpoints), 1, (0,0,0))
    player2health = statfont.render("Health: " + str(player[1].Lifepoints), 1, (0,0,0))
    player2stamina = statfont.render("Stamina: " + str(player[1].Conditionpoints), 1, (0,0,0))
    if len(player) >= 3:
        player3health = statfont.render("Health: " + str(player[2].Lifepoints), 1, (0,0,0))
        player3stamina = statfont.render("Stamina: " + str(player[2].Conditionpoints), 1, (0,0,0))
    if len(player) == 4:
        player4health = statfont.render("Health: " + str(player[3].Lifepoints), 1, (0,0,0))
        player4stamina = statfont.render("Stamina: " + str(player[3].Conditionpoints), 1, (0,0,0))

  
    screen.blit(player1health, (GetCenter(width, height, player1health)[0] - (width / 2.8), GetCenter(width,height, player1health)[1] - (height / 6.5) + 8))
    screen.blit(player1stamina, (GetCenter(width, height, player1stamina)[0] - (width / 2.8) + 22, GetCenter(width,height, player1stamina)[1] - (height / 6.5) + 66))
    screen.blit(player[0].Texture, (GetCenter(width, height, player1stamina)[0] - (width / 2.4) - 10 , GetCenter(width,height, player1stamina)[1] - (height / 6.5) + 25))
    screen.blit(player2health, (GetCenter(width, height, player2health)[0] - (width / 2.8), GetCenter(width,height, player2health)[1] - (height / 6.5) + 136))
    screen.blit(player2stamina, (GetCenter(width, height, player2stamina)[0] - (width / 2.8) + 22, GetCenter(width,height, player2stamina)[1] - (height / 6.5) + 194))
    screen.blit(player[1].Texture, (GetCenter(width, height, player2stamina)[0] - (width / 2.4) - 10 , GetCenter(width,height, player2stamina)[1] - (height / 6.5) + 153))
    if len(player) >= 3:
        screen.blit(player3health, (GetCenter(width, height, player3health)[0] - (width / 2.8), GetCenter(width,height, player3health)[1] - (height / 6.5) + 264))
        screen.blit(player3stamina, (GetCenter(width, height, player3stamina)[0] - (width / 2.8) + 22, GetCenter(width,height, player3stamina)[1] - (height / 6.5) + 322))
        screen.blit(player[2].Texture, (GetCenter(width, height, player3stamina)[0] - (width / 2.4) - 10 , GetCenter(width,height, player3stamina)[1] - (height / 6.5) + 281))
    if len(player) == 4:
        screen.blit(player4health, (GetCenter(width, height, player4health)[0] - (width / 2.8), GetCenter(width,height, player4health)[1] - (height / 6.5) + 392))
        screen.blit(player4stamina, (GetCenter(width, height, player4stamina)[0] - (width / 2.8) + 22, GetCenter(width,height, player4stamina)[1] - (height / 6.5) + 452))
        screen.blit(player[3].Texture, (GetCenter(width, height, player4stamina)[0] - (width / 2.4) - 10 , GetCenter(width,height, player4stamina)[1] - (height / 6.5) + 409))
