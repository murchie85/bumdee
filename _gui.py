import pygame
from _draw              import *

class gui():
    def __init__(self,
        white, 
        screen, 
        width, 
        height,
        smallNokiaFont,
        hugeNokiaFont,
        font,
        bigFont,
        hugeFont,
        smallFont,
        nanoFont,
        themeColour,
        exitButton,
        nextButton,
        dialogue,
        sDialogue,
        smsDialogue,
        music,
        borderSlides,
        clicked=False):

        self.white              = white
        self.screen             = screen
        self.width              = width
        self.height             = height
        self.smallNokiaFont     = smallNokiaFont
        self.hugeNokiaFont      = hugeNokiaFont
        self.font               = font
        self.bigFont            = bigFont
        self.hugeFont           = hugeFont
        self.smallFont          = smallFont
        self.nanoFont           = nanoFont
        self.themeColour        = themeColour
        self.exitButton         = exitButton
        self.nextButton         = nextButton
        self.dialogue           = dialogue
        self.sDialogue          = sDialogue
        self.smsDialogue        = smsDialogue
        self.music              = music
        self.borderSlides       = borderSlides
        self.clicked            = clicked

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


        
        self.signal             = pygame.image.load('pics/phoneLogos/signal.png')
        self.bottomNav          = pygame.image.load('pics/assets/mocks/navBottom.png')
        self.tileBackground     = pygame.image.load('pics/assets/backgrounds/tile.png')

        self.widgetNode         = [pygame.image.load('pics/assets/widgetNode/widgetNode1.png'),pygame.image.load('pics/assets/widgetNode/widgetNode2.png')] 
        self.widgetNode         = [pygame.image.load('pics/assets/widgetNode/widgetNode1.png'),pygame.image.load('pics/assets/widgetNode/widgetNode2.png')] 
        self.smallActiveWidget  = pygame.image.load('pics/assets/widgetNode/smallActiveWidget.png')
        self.medActiveWidget    = pygame.image.load('pics/assets/widgetNode/medActiveWidget.png')
        self.bigActiveWidget    = pygame.image.load('pics/assets/widgetNode/bigActiveWidget.png')
        
        self.extendableBox      = [pygame.image.load('pics/assets/textBox/extendableDarkGreen1.png'),pygame.image.load('pics/assets/textBox/extendableDarkGreen2.png')]


        self.signal          = pygame.image.load('pics/phoneLogos/signal.png')
        self.minis           = [pygame.image.load('pics/assets/minis/minibuttons1.png'),pygame.image.load('pics/assets/minis/minibuttons2.png'),pygame.image.load('pics/assets/minis/minibuttons3.png'),pygame.image.load('pics/assets/minis/minibuttons4.png'),pygame.image.load('pics/assets/minis/minibuttons5.png'),pygame.image.load('pics/assets/minis/minibuttons6.png'),pygame.image.load('pics/assets/minis/minibuttons7.png'),pygame.image.load('pics/assets/minis/minibuttons8.png'),pygame.image.load('pics/assets/minis/minibuttons9.png'),pygame.image.load('pics/assets/minis/minibuttons10.png')]

        self.mx     = 0
        self.my     = 0

        #buttons 
        self.bank              = [pygame.image.load('pics/assets/buttons/bank1.png'),pygame.image.load('pics/assets/buttons/bank2.png')]


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


    def showWidgNode(self,widgetNodeX,widgetNodeY,headerText="Widget",bodyText="Widget textX",selectable=True):
        selected = False
        selected = drawSelectableImage(self.widgetNode[0],self.widgetNode[1],(widgetNodeX,widgetNodeY),self,trim=False)
        widgetNodeW = self.widgetNode[0].get_rect().w

        

        hovered,tw,th= drawText(self.screen,self.nanoNokiaFont, headerText, widgetNodeX,widgetNodeY+8, self.greenD,center=widgetNodeW)
        drawText(self.screen,self.nanoNokiaFont, bodyText, widgetNodeX,widgetNodeY+37, self.greenD,center=widgetNodeW)
        
        if(selectable==False): return(False)
        
        return(selected)

    def incrementableWidget(self,x,y,text,value,inc=1):

        displayText = text + ' ' + str(value)
        selected = drawSelectableImage(self.minis[4],self.minis[5],(x,y),self,trim=False)
        if(selected):
            value = value + inc
        textx, texty = x+60,y+10
        hov, tw,ty = drawText(self.screen,self.nanoNokiaFont, displayText,textx ,texty, self.greenD)
        
        xEnd,yEnd = textx + tw, y + self.minis[5].get_rect().h

        return(value,xEnd,yEnd)






