from Node import *

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
  fighterlist = Node(sFighter("Wesley Sniper",10,12,14,16,14,12),fighterlist)
  fighterlist = Node(sFighter("Jet Ri",10,30,12,25,14,23),fighterlist)
  fighterlist = Node(sFighter("Steve Seagal",10,15,12,11,25,20),fighterlist)
  fightersist = Node(sFighter("Super Merio",10,10,30,30,15,15),fighterlist)
  fightersist = Node(sFighter("Vin Dieser",20,25,30,25,20,15),fighterlist)
  fightersist = Node(sFighter("Chack Norris",15,28,27,25,29,30),fighterlist)
  fightersist = Node(sFighter("The Roch",13,28,30,17,10,7),fighterlist)
