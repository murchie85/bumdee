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
        notificationDialogue,
        debugSwitch = True,
        clicked=False):

        self.white                  = white
        self.screen                 = screen
        self.width                  = width
        self.height                 = height
        self.smallNokiaFont         = smallNokiaFont
        self.hugeNokiaFont          = hugeNokiaFont
        self.font                   = font
        self.bigFont                = bigFont
        self.hugeFont               = hugeFont
        self.smallFont              = smallFont
        self.nanoFont               = nanoFont
        self.themeColour            = themeColour
        self.exitButton             = exitButton
        self.nextButton             = nextButton
        self.dialogue               = dialogue
        self.sDialogue              = sDialogue
        self.smsDialogue            = smsDialogue
        self.music                  = music
        self.borderSlides           = borderSlides
        self.notificationDialogue   = notificationDialogue
        self.clicked                = clicked
        self.debugSwitch            = debugSwitch

        self.greenA        = (36,65,45)
        self.greenB        = (82,128,58)
        self.greenC        = (173,195,63)
        self.greenD        = (215,233,149)
        self.darkGreen     = (5,37,23)
        self.buttonGreen   = (47,75,45)
        self.offwhite      = (245,245,245)
        self.screenDefault = (201,221,126)
        self.screenColour  = (201,221,126)


        self.greenText     = (29,153,29)
        self.greenBorder   = (127,187,73)
        self.darkGrey      = (44,52,56)
        self.lightBlack    = (40,41,35)
        self.lightGrey     = (72,77,79)


        # ---------------Images 


        # Intro 

        self.titleScreenImgs    = [pygame.image.load('pics/intro/intro1.png'),pygame.image.load('pics/intro/intro2.png')]




        self.signal             = pygame.image.load('pics/phoneLogos/signal.png')
        self.bottomNavMock      = pygame.image.load('pics/assets/mocks/navBottom.png')
        self.bottomNav          = pygame.image.load('pics/assets/nav/navBottom.png')
        self.nextDayBtn         = [pygame.image.load('pics/assets/nav/nextDay1.png'),pygame.image.load('pics/assets/nav/nextDay2.png')]
        self.tileBackground     = pygame.image.load('pics/assets/backgrounds/tile.png')

        self.widgetNode         = [pygame.image.load('pics/assets/widgetNode/widgetNode1.png'),pygame.image.load('pics/assets/widgetNode/widgetNode2.png'),pygame.image.load('pics/assets/widgetNode/widgetNode3.png')] 
        self.smallActiveWidget  = pygame.image.load('pics/assets/widgetNode/smallActiveWidget.png')
        
        self.medActiveWidget    = pygame.image.load('pics/assets/widgetNode/medActiveWidget.png')
        self.medActiveWidgetLab = pygame.image.load('pics/assets/widgetNode/widgetMedLabel.png')
        
        self.bigActiveWidget    = pygame.image.load('pics/assets/widgetNode/bigActiveWidget.png')
        
        self.extendableBox      = [pygame.image.load('pics/assets/textBox/extendableDarkGreen1.png'),pygame.image.load('pics/assets/textBox/extendableDarkGreen2.png')]

        self.notitfyBtnSmall    = [pygame.image.load('pics/assets/buttons/buttonSmall1.png'),pygame.image.load('pics/assets/buttons/buttonSmall2.png')]
        self.notitfyBtnMed      = [pygame.image.load('pics/assets/buttons/buttonMed1.png'),pygame.image.load('pics/assets/buttons/buttonMed2.png')]


        self.signal          = pygame.image.load('pics/phoneLogos/signal.png')
        self.minis           = [pygame.image.load('pics/assets/minis/minibuttons1.png'),pygame.image.load('pics/assets/minis/minibuttons2.png'),pygame.image.load('pics/assets/minis/minibuttons3.png'),pygame.image.load('pics/assets/minis/minibuttons4.png'),pygame.image.load('pics/assets/minis/minibuttons5.png'),pygame.image.load('pics/assets/minis/minibuttons6.png'),pygame.image.load('pics/assets/minis/minibuttons7.png'),pygame.image.load('pics/assets/minis/minibuttons8.png'),pygame.image.load('pics/assets/minis/minibuttons9.png'),pygame.image.load('pics/assets/minis/minibuttons10.png')]

        self.mx     = 0
        self.my     = 0

        #buttons 
        self.sell              = [pygame.image.load('pics/assets/buttons/sell1.png'),pygame.image.load('pics/assets/buttons/sell2.png')]


        self.menuBG = None
        self.hideExitButton    = False

    def border(self,colour=(128,0,0)):
        self.bx,self.by = 0.1*self.width,0.1*self.height
        self.bw,self.bh = 0.8*self.width,0.8*self.height
        rect = pygame.draw.rect(self.screen, colour, [self.bx, self.by,self.bw , self.bh],4)

    def mouseCollides(self,mousePos,x,y,w,h):
        if mousePos[0] > x and mousePos[0] < x + w:
            if mousePos[1] > y and mousePos[1] < y + h:
                return(True)
        return(False)



    def incrementableWidget(self,x,y,text,value,inc=1,cap=100):
        """+ button and text to increment and return value
        """

        displayText = text + ' ' + str(value)
        selected = drawSelectableImage(self.minis[4],self.minis[5],(x,y),self,trim=False)
        if(selected and inc<=cap):
            value = value + inc
        textx, texty = x+60,y+10
        hov, tw,ty = drawText(self.screen,self.nanoNokiaFont, displayText,textx ,texty, self.greenD)
        
        xEnd,yEnd = textx + tw, y + self.minis[5].get_rect().h

        return(value,xEnd,yEnd)


    def debug(self,debugMessage):
        if(self.debugSwitch):
            print(debugMessage)

    def debugDetailed(self,debugMessage):
        if(self.debugSwitch=='detailed'):
            print(debugMessage)



class notificationDialogue():
    def __init__(self):
        self.initialised = False
        self.origText    = ''
        self.origSource  = ''
        self.textArray   = []
        self.colour      = (0,0,0)
        self.y           = 0
        
        self.senPos      = 0

    def drawDialogue(self,gui,myfont, text,pos,maxWidth,maxHeight,clicked, colour=(255, 255, 255),skip=False,verticalSep=1.1,maxVerticleLines=80,displayNextButton=False,source=None):
        sx,sy = pos[0],pos[1]
        x,y        = sx,sy
        tRemaining = ""
        hovered    = gui.mouseCollides((gui.mx,gui.my),x,y,maxWidth,maxHeight)

        # reset if called by new function
        if(self.origText!= text or self.origSource!= source):
            self.initialised=False
            self.origText = text

        if(self.initialised== False):
            # format paragraph into array of fitted sentences
            self.origText    = text
            self.origSource  = source
            self.senPos      = 0
            dAr,para = [], ""
            for word in text.split(' '):
                pre   = para
                para += word + " "
                textsurface = myfont.render(para, True, colour)
                w = textsurface.get_rect().width
                if(w>= maxWidth):
                    dAr.append(pre)
                    para = word + " "
            dAr.append(para)

            self.textArray = dAr
            self.initialised = True
        


        hTotal = 0
        for sentence in range(0,len(self.textArray)):
            textsurface = myfont.render(self.textArray[sentence], True, colour)
            h = textsurface.get_rect().height
            gui.screen.blit(textsurface,(x,y))
            y = y + verticalSep*h
            hTotal = hTotal + verticalSep*h
            tRemaining = self.textArray[sentence+1:]

            # Condition: If lines exceed specified MAX LINES, break here
            if((sentence>=maxVerticleLines-1)): break

            # Condition: If lines exceed specified HEIGHT
            if(hTotal >= maxHeight): break

            #if(displayNextButton): nextP = gui.nextButton.display(gui,noBorder=False)

        # Condition: If lines remaining and clicked, go next page
        if(clicked and hovered and (len(tRemaining)>0)):
            self.textArray = tRemaining



