import pygame

def GetCenter(width,height,object):
    tempsize = object.get_rect().size
    resultwidth = (width / 2) - (tempsize[0] / 2)
    resultheight = (height / 2) - (tempsize[1] / 2)
    return (int(resultwidth), int(resultheight))