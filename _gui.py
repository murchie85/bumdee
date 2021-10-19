import pygame
from _draw import *

class gui():
    def __init__(self,white, screen, width, height,smallNokiaFont,hugeNokiaFont,font,bigFont,hugeFont,smallFont,nanoFont,themeColour,exitButton,nextButton,dialogue,sDialogue,smsDialogue,music,borderSlides,clicked=False):
        self.white           = white
        self.screen          = screen
        self.width           = width
        self.height          = height
        self.smallNokiaFont  = smallNokiaFont
        self.hugeNokiaFont   = hugeNokiaFont
        self.font            = font
        self.bigFont         = bigFont
        self.hugeFont        = hugeFont
        self.smallFont       = smallFont
        self.nanoFont        = nanoFont
        self.themeColour     = themeColour
        self.exitButton      = exitButton
        self.nextButton      = nextButton
        self.dialogue        = dialogue
        self.sDialogue       = sDialogue
        self.smsDialogue     = smsDialogue
        self.music           = music
        self.borderSlides    = borderSlides
        self.clicked         = clicked

        self.greenA        = (36,65,45)
        self.greenB        = (82,128,58)
        self.greenC        = (173,195,63)
        self.greenD        = (215,233,149)
        self.buttonGreen   = (47,75,45)
        self.screenDefault = (201,221,126)
        self.screenColour  = (201,221,126)

        self.greenText     = (29,153,29)
        self.greenBorder   = (127,187,73)
        self.darkGrey      = (44,52,56)
        self.lightBlack    = (40,41,35)
        self.lightGrey     = (72,77,79)


        
        self.signal        = pygame.image.load('pics/phoneLogos/signal.png')

        self.mx     = 0
        self.my     = 0


        self.menuBG = None

    def border(self,colour=(128,0,0)):
        self.bx,self.by = 0.1*self.width,0.1*self.height
        self.bw,self.bh = 0.8*self.width,0.8*self.height
        rect = pygame.draw.rect(self.screen, colour, [self.bx, self.by,self.bw , self.bh],4)

    def mouseCollides(self,mousePos,x,y,w,h):
        if mousePos[0] > x and mousePos[0] < x + w:
            if mousePos[1] > y and mousePos[1] < y + h:
                return(True)
        return(False)


class desktop():
    def __init__(self):
        self.button  = None
        self.flicker = 40
        self.flickD  = 40

    def drawDesktop(self,gui,gs,animateImgs):
        #gui.screen.fill(gui.darkGrey)
        gui.screen.fill(gui.greenA)

        # animate border 
        animateImgs.animate(gui,gs.state,gui.borderSlides,(0,15,15),(0,0))
        
        # draw clockbox
        boxx,boxy = 0.7*gui.width,1
        boxw,boxh = 0.3*gui.width,0.07*gui.height
        pygame.draw.rect(gui.screen, (0,0,0),         [boxx, boxy,boxw, boxh],border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, gui.greenBorder, [boxx, boxy,boxw, boxh],5,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        
        # draw clock
        day,date,month,time = gs.date[0],gs.date[1],gs.date[2],gs.date[3]
        textX    = boxx + 0.2*boxw
        h,tw,th  = drawText(gui.screen,gui.smallFont, day,textX,15, gui.greenText)
        textX    = textX + tw + 10
        h,tw,th  = drawText(gui.screen,gui.smallFont, date, textX,15, gui.greenText)
        textX    = textX + tw + 10
        h,tw,th  = drawText(gui.screen,gui.smallFont, month, textX,15, gui.greenText)
        textX    = textX + tw + 30
        self.flicker -=1
        if(self.flicker<1): self.flicker = self.flickD
        if(self.flicker>20):
            drawText(gui.screen,gui.smallFont, time, textX,15, gui.greenText)

        # SIGNAL ICON
        drawImage(gui.screen, gui.signal,(boxx + 0.04 *boxw,15))

        # -----------NAVIGATION BAR
        nbx,nby = 15,15
        nbW,nbH = 0.65*gui.width,0.13*gui.height
        fColour,bColour = (31,57,37),gui.greenB
        active = gui.mouseCollides((gui.mx,gui.my),nbx,nby,nbW,nbH)
        if(active):
            fColour,bColour = gui.darkGrey,gui.greenBorder

        pygame.draw.rect(gui.screen, fColour,[nbx, nby,nbW, nbH],border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, bColour,[nbx, nby,nbW, nbH],8,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        bx = nbx + 0.05*nbW
        by = nby + 0.2*nbH
        # Nav Buttons 
        statusButton = gui.statusButton.display(gui,fillColour=gui.buttonGreen,updatePos=(bx,by),hoverBoxCol=(61,111,67),hoverTextCol=gui.greenC)
        
        bx = bx + statusButton[1] + 0.25 * statusButton[1]
        InventoryButton  = gui.inventoryButton.display(gui,fillColour=gui.buttonGreen,updatePos=(bx,by),hoverBoxCol=(61,111,67),hoverTextCol=gui.greenC)
        
        bx = bx + InventoryButton[1] + 0.25 * InventoryButton[1]
        notificationButton = gui.noteButton.display(gui,fillColour=gui.buttonGreen,updatePos=(bx,by),hoverBoxCol=(61,111,67),hoverTextCol=gui.greenC)
        bh = notificationButton[2]
        
        
        # ------Black Info Box
        boxColour  = (0,0,0)
        boxHColour = gui.lightBlack

        infboxw  = 0.4*nbW
        infBoxh  = 1.2*bh
        infoBoxy = nby + 0.15*nbH
        bx = bx + notificationButton[1] + 2.2 * notificationButton[1]
        pygame.draw.rect(gui.screen, boxColour,[bx, infoBoxy,infboxw, infBoxh],border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, (55,95,73),[bx, infoBoxy,infboxw, infBoxh],2,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # write balance 
        moneyX,moneyY = bx + 0.10*infboxw, by + 0.1*infBoxh
        h,tw,th   = drawText(gui.screen,gui.smallNokiaFont, 'Balance',moneyX,moneyY, (89,207,147))
        h2,tw2,th = drawText(gui.screen,gui.smallNokiaFont, '£ '+str(gs.money),moneyX, moneyY + 0.31*infBoxh, (89,207,147))
        

        # write status
        healthX = moneyX + tw + (0.2*tw)
        healthY = moneyY
        h,tw,th = drawText(gui.screen,gui.smallNokiaFont, 'Status',healthX,moneyY, (89,207,147))
        h2,tw2,th = drawText(gui.screen,gui.smallNokiaFont, 'Surviving',healthX, moneyY + 0.31*infBoxh, (89,207,147))

        # write level
        lvX = healthX + 2*(tw)
        lvY = by + 0.12*infBoxh
        h3,tw3,th = drawText(gui.screen,gui.bigFont, 'Lv ' + str(gs.level),lvX, lvY, (89,207,147))

