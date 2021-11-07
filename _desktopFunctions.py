import pygame
from _draw import *



class meshFx():
    def __init__(self):
        self.horizontalLine = 'line'


    def drawLine(self,gui):
        x,y    = gui.width/2, 0
        x2,y2  = gui.width/2, gui.height
        pygame.draw.line(gui.screen, (255,255,255), (x, y), (x2, y2), 3)
 

class desktop():
    def __init__(self):
        self.button            = None
        self.flicker           = 40
        self.flickD            = 40
        self.overrideMessage   = None
        self.notificationTimer = 0
        self.infoboxVars       = [0,0,0,0,0,0,[0,0,0]]
        self.meshfx            = meshFx()


    def blackInfoBox(self,gui,gs,overrideMessage,notificationDisplayTime=2):

            bx,by,bh,nby,nbW,nbH,notificationButton = self.infoboxVars[0],self.infoboxVars[1],self.infoboxVars[2],self.infoboxVars[3],self.infoboxVars[4],self.infoboxVars[5],self.infoboxVars[6]

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
                self.notificationTimer += gs.dt/1000
                if(self.notificationTimer > notificationDisplayTime):
                    self.notificationTimer  = 0
                    self.overrideMessage    = None
                
                nx,ny = bx , by + 0.2*infBoxh
                drawText(gui.screen,gui.smallNokiaFont, overrideMessage,nx,ny, (89,207,147),center=infboxw)
                return()


            # write balance 
            gs.money = round(gs.money,2)
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

    def blackBoardOverride(self,conditionsArray,gui,gs):
        
        for condition in conditionsArray:

            conditionOne  = condition[0]
            conditionTwo  = condition[1]
            updateMessage = condition[2]
            
            if(conditionOne and conditionTwo):
                self.overrideMessage = updateMessage
                self.blackInfoBox(gui,gs,self.overrideMessage,notificationDisplayTime=5)




    def drawDesktop(self,gui,gs,animateImgs,phone):

        ######################################################
        #
        #                   DRAW SECTION
        #
        ######################################################


        gui.screen.fill(gui.greenA)
        #drawImage(gui.screen, gui.cubeBackground,(0,0))

        # animate border 
        #animateImgs.animate(gui,gs.state,gui.borderSlides,(0,15,15),(0,0))
        
        
        # draw clockbox
        boxx,boxy = 0.7*gui.width,1
        boxw,boxh = 0.3*gui.width,0.07*gui.height
        pygame.draw.rect(gui.screen, (0,0,0),         [boxx, boxy,boxw, boxh],border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        #pygame.draw.rect(gui.screen, gui.greenBorder, [boxx, boxy,boxw, boxh],5,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        

        # Draw border
        drawImage(gui.screen, gui.borderSlide,(0,0))

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
        fColour,bColour = gui.darkGrey,gui.greenBorder
        active = gui.mouseCollides((gui.mx,gui.my),nbx,nby,nbW,nbH)
        
        if(active): fColour,bColour = (31,57,37),gui.greenB
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
        bNavW,bNavH = gui.bottomNav.get_rect().w,gui.bottomNav.get_rect().h
        
        # ---- bottomnav
        navx, navy = 0.4* gui.width,gui.height - bNavH - 10
        drawImage(gui.screen, gui.bottomNav,(navx,navy))
        
        # ---- nextday
        navButtonW = gui.nextDayBtn[1].get_rect().w
        nextday = drawSelectableImage(gui.nextDayBtn[0],gui.nextDayBtn[1],(navx + bNavW - 1.5*navButtonW,navy + 0.2*bNavH),gui)
        
        #---- uncomment for showcase
        #drawImage(gui.screen, gui.bottomNavMock,(navx,navy))

        self.infoboxVars = [bx,by,bh,nby,nbW,nbH,notificationButton]

        # ------Black Info Box
        self.blackInfoBox(gui,gs,overrideMessage=self.overrideMessage)


        ######################################################
        #
        #                   LOGIC SECTION
        #
        ######################################################


        if((gs.halt)!=True and (gs.cutScene) != True and gs.notifyState =='inactive'):
            if(nextday):
                gui.debug('attempting to call next day')
                if(gs.eventState==None):
                    gui.debug('setting next day')
                    gs.eventState = 'nextDay'



        



        


        




