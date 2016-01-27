import pygame
from Getcenter import *
from GetRandomEvent import *
from Dice import *
def PlayerversusPlayer(screen,width,height,player1,player2):
  maincolor = (100,100,100)

  square = pygame.Surface((width - 200,height - 200), pygame.SRCALPHA, 32)
  outline = pygame.Surface((width - 190, height - 190), pygame.SRCALPHA, 32)
  #title = 
  square.fill(maincolor)
  outline.fill((0,0,0))
  screen.blit(outline, (GetCenter(width,height,outline)))
  screen.blit(square, (GetCenter(width,height,square)))
  pygame.display.flip()

def PlayerversusSuperfight(screen,width,height,player1,fighterlist):
  maincolor = (100,100,100)
  font = pygame.font.Font(None, 40)
  square = pygame.Surface((width - 200,height - 200), pygame.SRCALPHA, 32)
  outline = pygame.Surface((width - 190, height - 190), pygame.SRCALPHA, 32)
  square.fill(maincolor)
  outline.fill((0,0,0))
  screen.blit(outline, (GetCenter(width,height,outline)))
  screen.blit(square, (GetCenter(width,height,square)))
  fighter = ReturnSuperfighter(fighterlist)

  srolled = dice(6)

  if srolled == 1:
    sdmg = fighter.One
  elif srolled == 2:
    sdmg = fighter.Two
  elif srolled == 3:
    sdmg = fighter.Three
  elif srolled == 4:
    sdmg = fighter.Four
  elif srolled == 5:
    sdmg = fighter.Five
  elif srolled == 6:
    sdmg = fighter.Six  
  
  fightertext = font.render("Superfighter: " + fighter.Name, 1,(0,0,0))
  screen.blit(fightertext, (GetCenter(width,height,fightertext)[0],GetCenter(width,height,fightertext)[1] - (height / 3)))
  rolled = dice(6)
  rolltext = font.render(player1.name + " rolled " + str(rolled), 1,(0,0,0))
  
  screen.blit(rolltext, (GetCenter(width,height,rolltext)[0],GetCenter(width,height,rolltext)[1] - (height / 3) + 40))
  button = pygame.Surface((250,140), pygame.SRCALPHA, 32)
  buttonoutline = pygame.Surface((255,145), pygame.SRCALPHA, 32)
  button.fill((200,200,200))
  buttonoutline.fill((0,0,0))
  if rolled == 1:
    textButton1 = font.render("Dmg: " + str(player1.dmg.one.one.dmg) + " Cond: " + str(player1.dmg.one.one.cond), 1,(0,0,0))
    returnvalue1 = [player1.dmg.one.one.dmg, player1.dmg.one.one.cond, sdmg]
    textButton2 = font.render("Dmg: " + str(player1.dmg.one.two.dmg) + " Cond: " + str(player1.dmg.one.two.cond), 1,(0,0,0))
    returnvalue2 = [player1.dmg.one.two.dmg, player1.dmg.one.two.cond, sdmg]
    textButton3 = font.render("Dmg: " + str(player1.dmg.one.three.dmg) + " Cond: " + str(player1.dmg.one.three.cond), 1,(0,0,0))
    returnvalue3 = [player1.dmg.one.three.dmg, player1.dmg.one.three.cond, sdmg]
  elif rolled == 2:
    textButton1 = font.render("Dmg: " + str(player1.dmg.two.one.dmg) + " Cond: " + str(player1.dmg.two.one.cond), 1,(0,0,0))
    returnvalue1 = [player1.dmg.two.one.dmg, player1.dmg.two.one.cond, sdmg]
    textButton2 = font.render("Dmg: " + str(player1.dmg.two.two.dmg) + " Cond: " + str(player1.dmg.two.two.cond), 1,(0,0,0))
    returnvalue2 = [player1.dmg.two.two.dmg, player1.dmg.two.two.cond, sdmg]
    textButton3 = font.render("Dmg: " + str(player1.dmg.two.three.dmg) + " Cond: " + str(player1.dmg.two.three.cond), 1,(0,0,0))
    returnvalue3 = [player1.dmg.two.three.dmg, player1.dmg.two.three.cond, sdmg]
  elif rolled == 3:
    textButton1 = font.render("Dmg: " + str(player1.dmg.three.one.dmg) + " Cond: " + str(player1.dmg.three.one.cond), 1,(0,0,0))
    returnvalue1 = [player1.dmg.three.one.dmg, player1.dmg.three.one.cond, sdmg]
    textButton2 = font.render("Dmg: " + str(player1.dmg.three.two.dmg) + " Cond: " + str(player1.dmg.three.two.cond), 1,(0,0,0))
    returnvalue2 = [player1.dmg.three.two.dmg, player1.dmg.three.two.cond, sdmg]
    textButton3 = font.render("Dmg: " + str(player1.dmg.three.three.dmg) + " Cond: " + str(player1.dmg.three.three.cond), 1,(0,0,0))
    returnvalue3 = [player1.dmg.three.three.dmg, player1.dmg.three.three.cond, sdmg]
  elif rolled == 4:
    textButton1 = font.render("Dmg: " + str(player1.dmg.four.one.dmg) + " Cond: " + str(player1.dmg.four.one.cond), 1,(0,0,0))
    returnvalue1 = [player1.dmg.four.one.dmg, player1.dmg.four.one.cond, sdmg]
    textButton2 = font.render("Dmg: " + str(player1.dmg.four.two.dmg) + " Cond: " + str(player1.dmg.four.two.cond), 1,(0,0,0))
    returnvalue2 = [player1.dmg.four.two.dmg, player1.dmg.four.two.cond, sdmg]
    textButton3 = font.render("Dmg: " + str(player1.dmg.four.three.dmg) + " Cond: " + str(player1.dmg.four.three.cond), 1,(0,0,0))
    returnvalue3 = [player1.dmg.four.three.dmg, player1.dmg.four.three.cond, sdmg]
  elif rolled == 5:
    textButton1 = font.render("Dmg: " + str(player1.dmg.five.one.dmg) + " Cond: " + str(player1.dmg.five.one.cond), 1,(0,0,0))
    returnvalue1 = [player1.dmg.five.one.dmg, player1.dmg.five.one.cond, sdmg]
    textButton2 = font.render("Dmg: " + str(player1.dmg.five.two.dmg) + " Cond: " + str(player1.dmg.five.two.cond), 1,(0,0,0))
    returnvalue2 = [player1.dmg.five.two.dmg, player1.dmg.five.two.cond, sdmg]
    textButton3 = font.render("Dmg: " + str(player1.dmg.five.three.dmg) + " Cond: " + str(player1.dmg.five.three.cond), 1,(0,0,0))
    returnvalue3 = [player1.dmg.five.three.dmg, player1.dmg.five.three.cond, sdmg]
  elif rolled == 6:
    textButton1 = font.render("Dmg: " + str(player1.dmg.six.one.dmg) + " Cond: " + str(player1.dmg.six.one.cond), 1,(0,0,0))
    returnvalue1 = [player1.dmg.six.one.dmg, player1.dmg.six.one.cond, sdmg]
    textButton2 = font.render("Dmg: " + str(player1.dmg.six.two.dmg) + " Cond: " + str(player1.dmg.six.two.cond), 1,(0,0,0))
    returnvalue2 = [player1.dmg.six.two.dmg, player1.dmg.six.two.cond, sdmg]
    textButton3 = font.render("Dmg: " + str(player1.dmg.six.three.dmg) + " Cond: " + str(player1.dmg.six.three.cond), 1,(0,0,0))
    returnvalue3 = [player1.dmg.six.three.dmg, player1.dmg.six.three.cond, sdmg]
  done = False
  while not done:
    screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] - (width / 5), GetCenter(width,height,buttonoutline)[1]))
    screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)))
    screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] + (width / 5), GetCenter(width,height,buttonoutline)[1]))
    screen.blit(button, (GetCenter(width,height,button)[0] - (width / 5), GetCenter(width,height,button)[1]))
    screen.blit(button, (GetCenter(width,height,button)))
    screen.blit(button, (GetCenter(width,height,button)[0] + (width / 5), GetCenter(width,height,button)[1]))
    screen.blit(textButton1, (GetCenter(width,height,textButton1)[0] - (width / 5), GetCenter(width,height,textButton1)[1]))
    screen.blit(textButton2, (GetCenter(width,height,textButton2)))
    screen.blit(textButton3, (GetCenter(width,height,textButton3)[0] + (width / 5), GetCenter(width,height,textButton3)[1]))

    pygame.display.flip()