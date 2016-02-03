import pygame
from Getcenter import *
from GetRandomEvent import *
from fightrules import *
from Dice import *
import time

def Firstplayer(screen,width,height,player1):
    font = pygame.font.Font("content\\font\\retro.ttf", 30)
    smallfont = pygame.font.Font("content\\font\\fipps.TTF", 15)
    bg = pygame.transform.scale(pygame.image.load("content\\board.png"), (width,height))
    rolled = dice(6)
    drawDiceBL(rolled,width,height,screen)
    rolltext = font.render("Attacker: '" + player1.Name + "' rolled " + str(player1.Lifepoints)  + " health and " + str(player1.Conditionpoints) + " stamina", 1,(0,64,0))
    errtext = font.render("You have too little condition", 1,(242,7,7))
    screen.blit(rolltext, (GetCenter(width,height,rolltext)[0],GetCenter(width,height,rolltext)[1] - (height / 3) + 35))
    buttonh = pygame.Surface((250,140), pygame.SRCALPHA, 32)
    button = pygame.Surface((250,140), pygame.SRCALPHA, 32)
    buttonoutline = pygame.Surface((255,145), pygame.SRCALPHA, 32)
    pygame.display.flip()
    buttonh.fill((222,222,222))
    button.fill((200,200,200))
    buttonoutline.fill((0,0,0))
    textButton4 = smallfont.render("Do nothing",1,(64,0,0))
    time.sleep(0.5)
    if rolled == 1:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.one.one.dmg) + " Cond: " + str(player1.dmg.one.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.one.one.dmg, player1.dmg.one.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.one.two.dmg) + " Cond: " + str(player1.dmg.one.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.one.two.dmg, player1.dmg.one.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.one.three.dmg) + " Cond: " + str(player1.dmg.one.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.one.three.dmg, player1.dmg.one.three.cond]
    elif rolled == 2:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.two.one.dmg) + " Cond: " + str(player1.dmg.two.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.two.one.dmg, player1.dmg.two.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.two.two.dmg) + " Cond: " + str(player1.dmg.two.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.two.two.dmg, player1.dmg.two.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.two.three.dmg) + " Cond: " + str(player1.dmg.two.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.two.three.dmg, player1.dmg.two.three.cond]
    elif rolled == 3:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.three.one.dmg) + " Cond: " + str(player1.dmg.three.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.three.one.dmg, player1.dmg.three.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.three.two.dmg) + " Cond: " + str(player1.dmg.three.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.three.two.dmg, player1.dmg.three.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.three.three.dmg) + " Cond: " + str(player1.dmg.three.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.three.three.dmg, player1.dmg.three.three.cond]
    elif rolled == 4:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.four.one.dmg) + " Cond: " + str(player1.dmg.four.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.four.one.dmg, player1.dmg.four.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.four.two.dmg) + " Cond: " + str(player1.dmg.four.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.four.two.dmg, player1.dmg.four.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.four.three.dmg) + " Cond: " + str(player1.dmg.four.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.four.three.dmg, player1.dmg.four.three.cond]
    elif rolled == 5:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.five.one.dmg) + " Cond: " + str(player1.dmg.five.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.five.one.dmg, player1.dmg.five.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.five.two.dmg) + " Cond: " + str(player1.dmg.five.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.five.two.dmg, player1.dmg.five.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.five.three.dmg) + " Cond: " + str(player1.dmg.five.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.five.three.dmg, player1.dmg.five.three.cond]
    elif rolled == 6:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.six.one.dmg) + " Cond: " + str(player1.dmg.six.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.six.one.dmg, player1.dmg.six.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.six.two.dmg) + " Cond: " + str(player1.dmg.six.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.six.two.dmg, player1.dmg.six.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.six.three.dmg) + " Cond: " + str(player1.dmg.six.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.six.three.dmg, player1.dmg.six.three.cond]
  
    done = False
    while not done:
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] - (width / 5), GetCenter(width,height,buttonoutline)[1]))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] + (width / 5), GetCenter(width,height,buttonoutline)[1]))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0], GetCenter(width,height,buttonoutline)[1] + 150))
        screen.blit(button, (GetCenter(width,height,button)[0] - (width / 5), GetCenter(width,height,button)[1]))
        screen.blit(button, (GetCenter(width,height,button)))
        screen.blit(button, (GetCenter(width,height,button)[0] + (width / 5), GetCenter(width,height,button)[1]))
        screen.blit(button, (GetCenter(width,height,button)[0], GetCenter(width,height,button)[1] + 150))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0] - (width / 5),GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0] - (width / 5),GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0] + (width / 5),GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0] + (width / 5),GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1]+ 150)).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1] + 150))
        screen.blit(textButton1, (GetCenter(width,height,textButton1)[0] - (width / 5), GetCenter(width,height,textButton1)[1]))
        screen.blit(textButton2, (GetCenter(width,height,textButton2)))
        screen.blit(textButton3, (GetCenter(width,height,textButton3)[0] + (width / 5), GetCenter(width,height,textButton3)[1]))
        screen.blit(textButton4, (GetCenter(width,height,textButton4)[0], GetCenter(width,height,textButton4)[1] + 150))
    
        pygame.event.get()
        #Start Game
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0] - (width / 5), GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue1[1]:  
                return returnvalue1
                break
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=GetCenter(width,height,button)).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue2[1]:    
                return returnvalue2
                break
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0] + (width / 5), GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue3[1]:   
                return returnvalue3
                break
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0], GetCenter(width,height,button)[1] + 150)).collidepoint(pygame.mouse.get_pos())):
            return [0,0]
            #Add breaks
        pygame.display.flip()


def Secondplayer (screen,width,height,player1,otherplayer,damage):
    font = pygame.font.Font("content\\font\\retro.ttf", 30)
    smallfont = pygame.font.Font("content\\font\\fipps.TTF", 15)
    errtext = font.render("You have too little condition", 1,(242,7,7))
    textButton4 = smallfont.render("Do nothing",1,(64,0,0))
    bg = pygame.transform.scale(pygame.image.load("content\\board.png"), (width,height))
    rolled = dice(6)
    
    square = pygame.image.load("content\\eventscreen.png")
    screen.blit(square, (GetCenter(width,height,square)))
    pygame.display.flip()
    drawDiceBL(rolled,width,height,screen)
    rolltext = font.render("Defender: '" + player1.Name + "' has " + str(player1.Lifepoints) + " health and " + str(player1.Conditionpoints) + " stamina", 1,(0,64,0))
    memetext = font.render("Attacker: '" + otherplayer.Name + "' does " + str(damage) + " damage", 1,(128,0,0))
    screen.blit(rolltext, (GetCenter(width,height,rolltext)[0],GetCenter(width,height,rolltext)[1] - (height / 3) + 70))
    screen.blit(memetext, (GetCenter(width,height,memetext)[0],GetCenter(width,height,memetext)[1] - (height / 3)))
    pygame.display.flip()
    button = pygame.Surface((250,140), pygame.SRCALPHA, 32)
    buttonoutline = pygame.Surface((255,145), pygame.SRCALPHA, 32)
    buttonh = pygame.Surface((250,140), pygame.SRCALPHA, 32)
    buttonh.fill((222,222,222))
    button.fill((200,200,200))
    buttonoutline.fill((0,0,0))
    if rolled == 1:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.one.one.dmg) + " Cond: " + str(player1.dmg.one.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.one.one.dmg, player1.dmg.one.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.one.two.dmg) + " Cond: " + str(player1.dmg.one.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.one.two.dmg, player1.dmg.one.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.one.three.dmg) + " Cond: " + str(player1.dmg.one.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.one.three.dmg, player1.dmg.one.three.cond]
    elif rolled == 2:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.two.one.dmg) + " Cond: " + str(player1.dmg.two.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.two.one.dmg, player1.dmg.two.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.two.two.dmg) + " Cond: " + str(player1.dmg.two.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.two.two.dmg, player1.dmg.two.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.two.three.dmg) + " Cond: " + str(player1.dmg.two.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.two.three.dmg, player1.dmg.two.three.cond]
    elif rolled == 3:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.three.one.dmg) + " Cond: " + str(player1.dmg.three.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.three.one.dmg, player1.dmg.three.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.three.two.dmg) + " Cond: " + str(player1.dmg.three.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.three.two.dmg, player1.dmg.three.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.three.three.dmg) + " Cond: " + str(player1.dmg.three.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.three.three.dmg, player1.dmg.three.three.cond]
    elif rolled == 4:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.four.one.dmg) + " Cond: " + str(player1.dmg.four.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.four.one.dmg, player1.dmg.four.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.four.two.dmg) + " Cond: " + str(player1.dmg.four.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.four.two.dmg, player1.dmg.four.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.four.three.dmg) + " Cond: " + str(player1.dmg.four.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.four.three.dmg, player1.dmg.four.three.cond]
    elif rolled == 5:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.five.one.dmg) + " Cond: " + str(player1.dmg.five.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.five.one.dmg, player1.dmg.five.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.five.two.dmg) + " Cond: " + str(player1.dmg.five.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.five.two.dmg, player1.dmg.five.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.five.three.dmg) + " Cond: " + str(player1.dmg.five.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.five.three.dmg, player1.dmg.five.three.cond]
    elif rolled == 6:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.six.one.dmg) + " Cond: " + str(player1.dmg.six.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.six.one.dmg, player1.dmg.six.one.cond]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.six.two.dmg) + " Cond: " + str(player1.dmg.six.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.six.two.dmg, player1.dmg.six.two.cond]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.six.three.dmg) + " Cond: " + str(player1.dmg.six.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.six.three.dmg, player1.dmg.six.three.cond]
    done = False
    while not done:
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] - (width / 5), GetCenter(width,height,buttonoutline)[1]))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] + (width / 5), GetCenter(width,height,buttonoutline)[1]))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0], GetCenter(width,height,buttonoutline)[1] + 150))
        screen.blit(button, (GetCenter(width,height,button)[0] - (width / 5), GetCenter(width,height,button)[1]))
        screen.blit(button, (GetCenter(width,height,button)))
        screen.blit(button, (GetCenter(width,height,button)[0] + (width / 5), GetCenter(width,height,button)[1]))
        screen.blit(button, (GetCenter(width,height,button)[0], GetCenter(width,height,button)[1] + 150))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0] - (width / 5),GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0] - (width / 5),GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0] + (width / 5),GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0] + (width / 5),GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1]+ 150)).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1] + 150))
        screen.blit(textButton1, (GetCenter(width,height,textButton1)[0] - (width / 5), GetCenter(width,height,textButton1)[1]))
        screen.blit(textButton2, (GetCenter(width,height,textButton2)))
        screen.blit(textButton3, (GetCenter(width,height,textButton3)[0] + (width / 5), GetCenter(width,height,textButton3)[1]))
        screen.blit(textButton4, (GetCenter(width,height,textButton4)[0], GetCenter(width,height,textButton4)[1] + 150))
    
        pygame.event.get()
        #Start Game
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0] - (width / 5), GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue1[1]:  
                return returnvalue1
                break
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=GetCenter(width,height,button)).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue2[1]:    
                return returnvalue2
                break
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0] + (width / 5), GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue3[1]:   
                return returnvalue3
                break
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0], GetCenter(width,height,button)[1] + 150)).collidepoint(pygame.mouse.get_pos())):
            return [0,0]
        pygame.display.flip()
         
def PlayerversusPlayer(screen,width,height,attacker,defender):
    square = pygame.image.load("content\\eventscreen.png")
    screen.blit(square, (GetCenter(width,height,square)))
    pygame.display.flip()
    Attacker = Firstplayer(screen,width,height,attacker)
    Defender = Secondplayer(screen,width,height,defender,attacker,Attacker[0])
    return [Attacker[0],Attacker[1],Defender[0],Defender[1]]
    pygame.display.flip()

def PlayerversusSuperfight(screen,width,height,player1,fighterlist):
    pygame.init()
    maincolor = (100,100,100)
    font = pygame.font.Font("content\\font\\retro.ttf", 30)
    smallfont = pygame.font.Font("content\\font\\fipps.TTF", 15)
    square = pygame.image.load("content\\eventscreen.png")
    bg = pygame.transform.scale(pygame.image.load("content\\bordspel_background.png"), (width,height))
    textButton4 = smallfont.render("Do nothing",1,(64,0,0))
    screen.blit(square, (GetCenter(width,height,square)))

    fighter = ReturnSuperfighter(fighterlist)
    pygame.display.flip()
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
    print(srolled)
    fightertext = font.render("Superfighter '" + fighter.Name + "' will do " + str(sdmg) + " damage", 1,(128,0,0))
  
    rolled = dice(6)
    drawDiceBL(rolled,width,height,screen)
    screen.blit(fightertext, (GetCenter(width,height,fightertext)[0],GetCenter(width,height,fightertext)[1] - (height / 3)))
    rolltext = font.render("'" + player1.Name + "'" + " has " + str(player1.Lifepoints) + " health and " + str(player1.Conditionpoints) + " stamina", 1,(0,64,0))
    errtext = font.render("You have too little condition", 1,(242,7,7))
    screen.blit(rolltext, (GetCenter(width,height,rolltext)[0],GetCenter(width,height,rolltext)[1] - (height / 3) + 70))
    button = pygame.Surface((250,140), pygame.SRCALPHA, 32)
    buttonoutline = pygame.Surface((255,145), pygame.SRCALPHA, 32)
    buttonh = pygame.Surface((250,140), pygame.SRCALPHA, 32)
    buttonh.fill((222,222,222))
    button.fill((190,190,190))
    buttonoutline.fill((0,0,0))
    
    if rolled == 1:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.one.one.dmg) + " Cond: " + str(player1.dmg.one.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.one.one.dmg, player1.dmg.one.one.cond, sdmg]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.one.two.dmg) + " Cond: " + str(player1.dmg.one.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.one.two.dmg, player1.dmg.one.two.cond, sdmg]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.one.three.dmg) + " Cond: " + str(player1.dmg.one.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.one.three.dmg, player1.dmg.one.three.cond, sdmg]
    elif rolled == 2:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.two.one.dmg) + " Cond: " + str(player1.dmg.two.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.two.one.dmg, player1.dmg.two.one.cond, sdmg]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.two.two.dmg) + " Cond: " + str(player1.dmg.two.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.two.two.dmg, player1.dmg.two.two.cond, sdmg]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.two.three.dmg) + " Cond: " + str(player1.dmg.two.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.two.three.dmg, player1.dmg.two.three.cond, sdmg]
    elif rolled == 3:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.three.one.dmg) + " Cond: " + str(player1.dmg.three.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.three.one.dmg, player1.dmg.three.one.cond, sdmg]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.three.two.dmg) + " Cond: " + str(player1.dmg.three.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.three.two.dmg, player1.dmg.three.two.cond, sdmg]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.three.three.dmg) + " Cond: " + str(player1.dmg.three.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.three.three.dmg, player1.dmg.three.three.cond, sdmg]
    elif rolled == 4:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.four.one.dmg) + " Cond: " + str(player1.dmg.four.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.four.one.dmg, player1.dmg.four.one.cond, sdmg]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.four.two.dmg) + " Cond: " + str(player1.dmg.four.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.four.two.dmg, player1.dmg.four.two.cond, sdmg]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.four.three.dmg) + " Cond: " + str(player1.dmg.four.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.four.three.dmg, player1.dmg.four.three.cond, sdmg]
    elif rolled == 5:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.five.one.dmg) + " Cond: " + str(player1.dmg.five.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.five.one.dmg, player1.dmg.five.one.cond, sdmg]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.five.two.dmg) + " Cond: " + str(player1.dmg.five.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.five.two.dmg, player1.dmg.five.two.cond, sdmg]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.five.three.dmg) + " Cond: " + str(player1.dmg.five.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.five.three.dmg, player1.dmg.five.three.cond, sdmg]
    elif rolled == 6:
        textButton1 = smallfont.render("Dmg: " + str(player1.dmg.six.one.dmg) + " Cond: " + str(player1.dmg.six.one.cond), 1,(0,0,0))
        returnvalue1 = [player1.dmg.six.one.dmg, player1.dmg.six.one.cond, sdmg]
        textButton2 = smallfont.render("Dmg: " + str(player1.dmg.six.two.dmg) + " Cond: " + str(player1.dmg.six.two.cond), 1,(0,0,0))
        returnvalue2 = [player1.dmg.six.two.dmg, player1.dmg.six.two.cond, sdmg]
        textButton3 = smallfont.render("Dmg: " + str(player1.dmg.six.three.dmg) + " Cond: " + str(player1.dmg.six.three.cond), 1,(0,0,0))
        returnvalue3 = [player1.dmg.six.three.dmg, player1.dmg.six.three.cond, sdmg]
    done = False
    while not done:
        
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] - (width / 5), GetCenter(width,height,buttonoutline)[1]))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0] + (width / 5), GetCenter(width,height,buttonoutline)[1]))
        screen.blit(buttonoutline, (GetCenter(width,height,buttonoutline)[0], GetCenter(width,height,buttonoutline)[1] + 150))
        screen.blit(button, (GetCenter(width,height,button)[0] - (width / 5), GetCenter(width,height,button)[1]))
        screen.blit(button, (GetCenter(width,height,button)))
        screen.blit(button, (GetCenter(width,height,button)[0] + (width / 5), GetCenter(width,height,button)[1]))
        screen.blit(button, (GetCenter(width,height,button)[0], GetCenter(width,height,button)[1] + 150))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0] - (width / 5),GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0] - (width / 5),GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0] + (width / 5),GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0] + (width / 5),GetCenter(width,height,button)[1]))
        if button.get_rect(topleft=(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1]+ 150)).collidepoint(pygame.mouse.get_pos()):
            screen.blit(buttonh,(GetCenter(width,height,button)[0],GetCenter(width,height,button)[1] + 150))

        screen.blit(textButton1, (GetCenter(width,height,textButton1)[0] - (width / 5), GetCenter(width,height,textButton1)[1]))
        screen.blit(textButton2, (GetCenter(width,height,textButton2)))
        screen.blit(textButton3, (GetCenter(width,height,textButton3)[0] + (width / 5), GetCenter(width,height,textButton3)[1]))
        screen.blit(textButton4, (GetCenter(width,height,textButton4)[0], GetCenter(width,height,textButton4)[1] + 150))
    
        pygame.event.get()
        #Start Game
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0] - (width / 5), GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue1[1]:  
                return returnvalue1
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=GetCenter(width,height,button)).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue2[1]:    
                return returnvalue2
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0] + (width / 5), GetCenter(width,height,button)[1])).collidepoint(pygame.mouse.get_pos())):
            if player1.Conditionpoints >= returnvalue3[1]:
                return returnvalue3
            else:
                screen.blit(errtext, (GetCenter(width,height,errtext)[0],GetCenter(width,height,errtext)[1] + (height / 3) - 70))
        if (pygame.mouse.get_pressed()==(1,0,0)  and button.get_rect(topleft=(GetCenter(width,height,button)[0], GetCenter(width,height,button)[1] + 150)).collidepoint(pygame.mouse.get_pos())):
            return [0,0,sdmg]
        pygame.display.flip()
        time.sleep(0.033)

def UltraPVP(screen,width,height,attacker,defender):
  memes = random.randint(0,1)
  if memes == 1:
    return pvp(attacker,defender,PlayerversusPlayer(screen,width,height,attacker,defender))
  else:
    return pvp(defender,attacker,PlayerversusPlayer(screen,width,height,defender,attacker))
