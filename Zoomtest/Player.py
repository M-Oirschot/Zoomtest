import random
 
class Player:
    def __init__(self, x, y, lifepoints, conditionpoints, texture, name, dmglist):
        self.Y = y
        self.X = x
        self.Lifepoints = lifepoints
        self.Conditionpoints = conditionpoints
        self.Texture = texture
        self.Name = name
        self.dmglist = dmglist


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

MT = dmg(one = dmgList(one = dmgItem(3, 1), two = dmgItem(9, 2), three = dmgItem(19, 3)), 
         two = dmgList(one = dmgItem(5, 2), two = dmgItem(11, 3), three = dmgItem(15, 5)), 
         three = dmgList(one = dmgItem(7, 3), two = dmgItem(12, 3), three = dmgItem(16, 4)),
         four = dmgList(one = dmgItem(2, 1), two = dmgItem(2, 1), three = dmgItem(6, 3)),
         five = dmgList(one = dmgItem(10, 2), two = dmgItem(20, 5), three = dmgItem(30, 8)),
         six = dmgList(one = dmgItem(8, 3), two = dmgItem(13, 4), three = dmgItem(17, 5)))
