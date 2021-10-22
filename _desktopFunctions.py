import pygame
from _draw import *


def blackInfoBox(desktop,gui,gs,bx,by,bh,nby,nbW,nbH,notificationButton,overrideMessage,notificationDisplayTime=1):

        # ------dimensions
        boxColour  = (0,0,0)
        boxHColour = gui.lightBlack
        infboxw  = 0.4*nbW
        infBoxh  = 1.2*bh
        infoBoxy = nby + 0.15*nbH
        bx = bx + notificationButton[1] + 2.2 * notificationButton[1]


        # -------draw box

        pygame.draw.rect(gui.screen, boxColour,[bx, infoBoxy,infboxw, infBoxh],border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, (55,95,73),[bx, infoBoxy,infboxw, infBoxh],2,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # ------ override message
        if(overrideMessage!=None):
            desktop.notificationTimer += gs.dt/1000
            if(desktop.notificationTimer > notificationDisplayTime):
                desktop.notificationTimer  = 0
                desktop.overrideMessage    = None
            
            nx,ny = bx , by + 0.2*infBoxh
            drawText(gui.screen,gui.smallNokiaFont, overrideMessage,nx,ny, (89,207,147),center=infboxw)
            return()


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


class desktop():
    def __init__(self):
        self.button            = None
        self.flicker           = 40
        self.flickD            = 40
        self.overrideMessage   = None
        self.notificationTimer = 0

    def drawDesktop(self,gui,gs,animateImgs,phone):
        #gui.screen.fill(gui.darkGrey)
        gui.screen.fill(gui.greenA)
        #drawImage(gui.screen, gui.tileBackground,(0,0))

        # animate border 
        animateImgs.animate(gui,gs.state,gui.borderSlides,(0,15,15),(0,0))
        
        # draw clockbox
        boxx,boxy = 0.7*gui.width,1
        boxw,boxh = 0.3*gui.width,0.07*gui.height
        pygame.draw.rect(gui.screen, (0,0,0),         [boxx, boxy,boxw, boxh],border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, gui.greenBorder, [boxx, boxy,boxw, boxh],5,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        
        # draw clock
        day,date,month,time = gs.displayDate[0],gs.displayDate[1],gs.displayDate[2],gs.displayDate[3]
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
        
        
        # ------Bottom Nav
        bNavH = gui.bottomNav.get_rect().h
        drawImage(gui.screen, gui.bottomNav,(0.4* gui.width,gui.height - bNavH - 10))

        # ------Black Info Box

        blackInfoBox(self,gui,gs,bx,by,bh,nby,nbW,nbH,notificationButton,overrideMessage=self.overrideMessage)
        


        



def bank(gs,desktop):
    moneyEarned = gs.cantabs * gs.exchangeRate
    
    gs.money   += moneyEarned
    gs.cantabs = 0
    gs.money   = round(gs.money,2)

    me =  "{:.2f}".format(moneyEarned)
    desktop.overrideMessage = "Banked £ " + str(me)

    # TOdo display popup




def pullTab(gui,phone,gs,fx,desktop):

    selected   = False 
    selectable = True

    # ----------Draw Pull Tab Widget 

    freeHorizontalWidth = gui.width - phone.mobileW - 100
    
    widgetNodeW = gui.widgetNode[0].get_rect().w
    widgetNodeX = phone.mobilex + phone.mobileW + 0.5* widgetNodeW
    widgetNodeY = phone.mobiley + 50
    
    # If a widget is active disable all others
    if(gs.activeWidget!=None): selectable = False 
    
    selected = gui.showWidgNode(widgetNodeX,widgetNodeY,headerText="Pull Tab",bodyText="Tabs Collected: " + str(gs.cantabs),selectable=selectable)

    if(selected): gs.activeWidget = 'pullTab'

    if(gs.activeWidget=='pullTab'):
        c = fx.fadeOut(gui,inc=40,alpha=100)
        # draw screen window
        drawImage(gui.screen, gui.medActiveWidget,(widgetNodeX,widgetNodeY))



        #-----------PICK UP TAB 
        incWidx, incWidy = widgetNodeX+50,1.7*widgetNodeY
        gs.cantabs, endX, endY =  gui.incrementableWidget(incWidx,incWidy,'Picked up', gs.cantabs)

        #-----------BANK
        
        gui.bank[0]
        bankX,bankY = incWidx,endY + 1 * gui.bank[0].get_rect().h

        bankSelected = drawSelectableImage(gui.bank[0],gui.bank[1],(bankX,bankY),gui,trim=False)
        if(bankSelected):
            bank(gs,desktop)

            # update message and set alert
            message = [11,'Unknown', 'What are you doing?','pics/characters/unknown.png']
            phone.messageUpdate(message,gui,gs,alert=True)
            
            





        # exit box
        exitX = widgetNodeX + gui.medActiveWidget.get_rect().w - 1.5*gui.minis[8].get_rect().w
        exitY = 1.4*widgetNodeY + gui.minis[8].get_rect().y
        selected = drawSelectableImage(gui.minis[8],gui.minis[9],(exitX,exitY),gui,trim=False)
        if(selected):
            gs.activeWidget = None

