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
  fighterlist = Node(sFighter("Jackie Chen", 12,10,15,9,10,25), fighterlist)
  fighterlist = Node(sFighter("Agua Man", 12,15,9,7,7,13), fighterlist)
  fighterlist = Node(sFighter("John Cena", 10,6,25,7,8,11), fighterlist)
  fighterlist = Node(sFighter("Pariz Hiltin", 12,8,7,15,13,9), fighterlist)
  fighterlist = Node(sFighter("Dexter", 9,8,7,15,13,9), fighterlist)
  fighterlist = Node(sFighter("Steve Urkel", 10,5,12,11,15,8), fighterlist)
  fighterlist = Node(sFighter("Ernold Schwarzenegger", 25,25,20,15,15,10), fighterlist)
  fighterlist = Node(sFighter("James Bend", 25,15,15,7,20,25), fighterlist)

