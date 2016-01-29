import random 

class Player:
    def __init__(self,starting, lifepoints, conditionpoints, texture, name, dmg):
        self.Starting = starting
        self.Lifepoints = lifepoints
        self.Conditionpoints = conditionpoints
        self.Texture = texture
        self.Name = name
        self.dmg = dmg
        self.Pos = starting

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

def MakePlayer(x,health,condition,texture,name,playernum):
  if playernum == 1:
    return Player(x,health,condition,texture,name,dmg(dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)), 
                                                    dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15, 5)), 
                                                    dmgList(dmgItem(7, 3), dmgItem(12, 3), dmgItem(16, 4)),
                                                    dmgList(dmgItem(2, 1), dmgItem(2, 1), dmgItem(6, 3)),
                                                    dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8)),
                                                    dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5))))
  if playernum  == 2:
    return Player(x,health,condition,texture,name,dmg(dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15, 5)), 
                                                    dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)), 
                                                    dmgList(dmgItem(2, 1), dmgItem(4, 2), dmgItem(6, 4)),
                                                    dmgList(dmgItem(7, 2), dmgItem(12, 3), dmgItem(16, 4)),
                                                    dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5)),
                                                    dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8))))
  if playernum == 3:
    return Player(x,health,condition,texture,name,dmg(dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8)), 
                                                    dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5)), 
                                                    dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)),
                                                    dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15,5)),
                                                    dmgList(dmgItem(7, 2), dmgItem(12, 3), dmgItem(16, 4)),
                                                    dmgList(dmgItem(2, 1), dmgItem(4, 2), dmgItem(6, 3))))
  if playernum == 4:
    return Player(x,health,condition,texture,name,dmg(dmgList(dmgItem(8, 3), dmgItem(13, 4), dmgItem(17, 5)), 
                                                    dmgList(dmgItem(10, 2), dmgItem(20, 5), dmgItem(30, 8)), 
                                                    dmgList(dmgItem(5, 2), dmgItem(11, 3), dmgItem(15, 5)),
                                                    dmgList(dmgItem(3, 1), dmgItem(9, 2), dmgItem(19, 3)),
                                                    dmgList(dmgItem(2, 1), dmgItem(4, 2), dmgItem(6, 3)),
                                                    dmgList(dmgItem(7, 2), dmgItem(12, 3), dmgItem(16, 4))))
