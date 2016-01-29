from Node import *
import random
class sFighter:
    def __init__(self,name,one,two,three,four,five,six):
        self.Name = name
        self.One = one
        self.Two = two
        self.Three = three
        self.Four = four
        self.Five = five
        self.Six = six

def MakeList():
    fighterlist = Empty
    fighterlist = Node(sFighter("Terry Crews",10,15,25,20,15,10),fighterlist)
    fighterlist = Node(sFighter("Jason Statham",15,17,19,21,23,26),fighterlist)
    fighterlist = Node(sFighter("Bruce Hee", 20,15,5,7,8,16), fighterlist)
    fighterlist = Node(sFighter("Jackie Chen", 12,10,15,9,10,25), fighterlist)
    fighterlist = Node(sFighter("Agua Man", 12,15,9,7,7,13), fighterlist)
    fighterlist = Node(sFighter("John Cena", 10,6,25,7,8,11), fighterlist)
    fighterlist = Node(sFighter("Pariz Hiltin", 12,8,7,15,13,9), fighterlist)
    fighterlist = Node(sFighter("Dexter", 9,8,7,15,13,9), fighterlist)
    fighterlist = Node(sFighter("Steve Urkel", 10,5,12,11,15,8), fighterlist)
    fighterlist = Node(sFighter("Ernold Schwarzenegger", 25,25,20,15,15,10), fighterlist)
    fighterlist = Node(sFighter("James Bend", 25,15,15,7,20,25), fighterlist)
    fighterlist = Node(sFighter("Wesley Sniper",10,12,14,16,14,12),fighterlist)
    fighterlist = Node(sFighter("Jet Ri",10,30,12,25,14,23),fighterlist)
    fighterlist = Node(sFighter("Steve Seagal",10,15,12,11,25,20),fighterlist)
    fighterlist = Node(sFighter("Super Merio",10,10,30,30,15,15),fighterlist)
    fighterlist = Node(sFighter("Vin Dieser",20,25,30,25,20,15),fighterlist)
    fighterlist = Node(sFighter("Chack Norris",15,28,27,25,29,30),fighterlist)
    fighterlist = Node(sFighter("The Roch",13,28,30,17,10,7),fighterlist)
    return fighterlist

def getItemFromList(list,position,zero):
    var = zero
    pos = position
    if var == pos:
        return list.Value
    else:
        return getItemFromList(list.Tail,position,var + 1)

def countList(list):
    if list.IsEmpty:
        return 0
    else:
        return countList(list.Tail) + 1

def ReturnSuperfighter(list):
    randomCard = random.randint(0,countList(list) - 1)
    print(randomCard)
    return getItemFromList(list,randomCard,0)
  