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