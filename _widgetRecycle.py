import pygame
from _draw import *
from _utils import *




class junkCollection():
    def __init__(self,w,x,y,winX,winY,winH,winW):
        self.w                      = w
        self.x                      = x
        self.y                      = y
        self.winX                   = winX
        self.winY                   = winY
        self.winH                   = winH
        self.winW                   = winW


        self.activeSubWidget            = 0
        self.totalSubWidgets            = 2


        self.tabsSold                   = False
        self.tabSellSelected            = False
        self.tabLimitReached            = False
        self.tabStopTimer               = stopTimer()
        
        self.capsSold                   = False
        self.capSellSelected            = False
        self.capLimitReached            = False
        self.capStopTimer               = stopTimer()


        self.cansSold                   = False
        self.canSellSelected            = False
        self.canLimitReached            = False
        self.canStopTimer               = stopTimer()



        self.notificationDisplayTime = 2
        self.stopTimer               =  stopTimer()


        

    def drawWindow(self,gui,phone,gs,tabNo,h1,h2,lPairArray,rPairArray):
        exitX       = self.winX + 0.92*self.winW
        exitY       = self.winY + 0.03*self.winH
        hedx        = self.winX + 0.6*self.winH
        hedy        = self.winY + 0.02*self.winH
        cptx        = self.winX + 0.18*self.winW
        cpty        = self.winY + 0.11*self.winH
        tbspx       = self.winX + 0.20*self.winW
        tbspy       = self.winY + 0.25*self.winH
        tbscy       = self.winY + 0.40*self.winH
        lineColour  = (45,113,70)
        LeftXMargin = self.winX+0.2*self.winW

        # --------draw gui

        drawSelectableImage(gui.mechBoxMed[tabNo],gui.mechBoxMed[tabNo],(self.winX,self.winY),gui)


        # ------- Change Widgets
        if(gui.user_input.returnedKey =='down'):
            self.activeSubWidget = self.activeSubWidget + 1
            gui.user_input.returnedKey =''
        if(gui.user_input.returnedKey =='up'):
            self.activeSubWidget = self.activeSubWidget - 1
            gui.user_input.returnedKey =''
        if(self.activeSubWidget>self.totalSubWidgets-1): self.activeSubWidget=0
        if(self.activeSubWidget<0): self.activeSubWidget=self.totalSubWidgets-1


        # ----------Heading 
        drawText(gui.screen,gui.squareFontH, h1,hedx,hedy, colour=(205, 230, 180))
        drawText(gui.screen,gui.squareFont, h2,cptx,cpty, colour=(205, 230, 180))
        xend,yend=drawTextandBoxGrid(gui.screen,gui.nanoNokiaFont,tbspx,tbspy, lPairArray,lineColour=(45,102,66))
        drawTextandBoxGrid(gui.screen,gui.nanoNokiaFont,xend + 70,tbspy, rPairArray,lineColour=lineColour )
          


        # --------exit if clicked outside
        if(((gui.mouseCollides((gui.mx,gui.my),self.winX,self.winY,self.winW,self.winH)) == False) and gui.clicked):
            gs.ACTIVEWIDGET = None

        # ---------Exit Window
        if(gui.mouseCollides((gui.mx,gui.my),exitX,exitY,40,40)):
            exitSelected = drawSelectableImage(gui.mechBoxMed[-1],gui.mechBoxMed[-1],(self.winX,self.winY),gui)
            if(exitSelected):
                gs.ACTIVEWIDGET = None

        return(self.winX,self.winY,self.winW,self.winH)
    

    def buyMagnets(self,magnetX,magnetY,gs,gui,desktop):

        # --------Unlock Magnets

        if((gs.totalCantabs + gs.totalCaps + gs.totalCans > 3) and (gs.totalCantabs + gs.totalCaps + gs.totalCans < 50)):
            if(gs.notifyPlayer("You can now Purchase magnets.")): gs.magnetsEnabled = True

        
        if(gs.magnets>-1 and gs.magnetsEnabled):
            buyMagnetSelected = drawTxtBtn(gui.mechBtnMed[0],gui.mechBtnMed[1],(magnetX,magnetY),gui,'Magnet',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
            if(buyMagnetSelected): 
                if(gs.money - gs.magnetPrice >0):
                    gs.money -= gs.magnetPrice
                    gs.money = round(gs.money,2)
                    gs.magnets +=1
                    desktop.overrideMessage = 'Magnet Purchased'
                else:
                    desktop.overrideMessage = 'Not enough credits'


    def autoCollect(self,value,valueEnabled,gs,cap,timer,delay=10,inc=1):
        delay = 1/delay
        # need to update for tab/cap and can
        if(valueEnabled):
            StopTimer = timer.stopWatch(delay,str(str('autoCollect') + str(value)),value,gs)
            if(StopTimer):
                if(inc<=cap):
                    value = int(value + inc)

        return(value)


    
    def recycleCenter(self,gui,gs,fx,desktop,phone):

        if(gs.ACTIVEWIDGET=='recycleCenter'):
            c = fx.fadeOut(gui,inc=40,alpha=100)

        if(self.activeSubWidget==0):
            # Only Run if widget selected
            if(gs.ACTIVEWIDGET=='recycleCenter'):

                lPairArray = [ ("Tabs Price", '£ '+ '{:.2f}'.format(gs.tabExchangeRate)),("Tabs Collected", str(gs.totalCantabs)),('AutoTab', str(gs.autoTab))]
                rPairArray = [("Limit", str(gs.cantabLimit)),('Level',str(gs.recycleLevel)),("Magnets",str(gs.magnets)),('scrap',str(gs.scrap)) ]
                winX,winY,winW,winH = self.drawWindow(gui,phone,gs,self.activeSubWidget,'Recycling Center','Can Pull Tabs',lPairArray,rPairArray)

                # --------DIMENSIONS
                
                collX       = winX + 0.20*winW
                collY       = winY + 0.7*winH
                sellX       = collX
                sellY       = collY + 0.1*winH
                autoX       = collX   + 0.24*winW
                autoY       = collY + 0.1*winH
                magnetX     = collX   + 0.4*winW
                magnetY     = collY
                abX         = collX   + 0.42*winW
                abY         = collY + 0.1*winH



                # ------Auto Buy
                
                gs.tabInstaBuy,txEnd,tyEnd = drawTxtBtnOnOff(gui.selectMe[0],gui.selectMe[1],(abX,abY),gs.tabInstaBuy,gui,'AutoBuy',font=gui.nanoNokiaFont,yadj=0.6,xadj=0.6)
                
                #-----------INC WIDGET: COLLECT 

                if(gs.totalCantabs<gs.cantabLimit):
                    cap = gs.cantabLimit - (gs.totalCantabs + gs.cantabs)
                    inc = 1 + gs.magnets
                    
                    #value incremented 
                    gs.cantabs, endX, endY =  gui.incrementableWidget(collX,collY,'Picked up', gs.cantabs,inc=inc,cap=cap,userInput=gui.user_input.returnedKey,incrementKey='c',insta=gs.tabInstaBuy,instaMessage='AutoBuy on')

                    # Sell button
                    self.tabSellSelected   = drawSelectableImage(gui.bank[0],gui.bank[1],(sellX,sellY),gui,trim=False)

                # -----------------buyMagnets
                self.buyMagnets(magnetX,magnetY,gs,gui,desktop)
                # -------------scrap %
                gs.scrapTabSplit, endX, endY =  gui.incDecWidgetAbsolute(collX,collY - 60,'Scrap %', gs.scrapTabSplit,inc=10,cap=100)

                # -----------------Auto
                if(drawSelectableImage(gui.auto[0],gui.auto[1],(autoX,autoY),gui)==True):
                    print('enabling auto')
                    gs.autoTabEnabled = True
        

                # ----- Continuously call DISABLE SELL
                if(self.tabLimitReached):
                    self.tabSellSelected                 = False
                    drawText(gui.screen,gui.nanoNokiaFont, "Current Limit Reached",collX,collY, colour=(50,50,50))
                

        # ------------------BackgroundJobs
        gs.cantabs = self.autoCollect(gs.cantabs,gs.autoTabEnabled,gs,(gs.cantabLimit - (gs.totalCantabs + gs.cantabs)),self.tabStopTimer,delay=gs.autoTab,inc = (1 + gs.magnets))

        # ----- SET LIMIT REACHED FLAG ONCE ONLY

        if((gs.totalCantabs>=gs.cantabLimit) and (self.tabLimitReached==False)):
            # call once only
            self.tabLimitReached         = True
            desktop.overrideMessage      = 'Limit reached'
            self.notificationDisplayTime = 6
            gs.tabRestrictedDate     = gs.gameTime.copy()
            
            # First and only limit message
            if((gs.cantabLimit==gs.tabLimits[0])):
                gs.notifyPlayer("Your have reached your limit, it will reset the following day. Note, not all limits reset the following day.")


        # ----- RESET ONE DAY LATER
        if(self.tabLimitReached):
            # time passed 
            daysPassed = gs.gameTime['daysPassed'] - gs.tabRestrictedDate['daysPassed']
            if(daysPassed>0):
                if(gs.cantabLimit<gs.tabLimits[-1]):
                    gs.cantabLimit = gs.tabLimits[gs.tabLimits.index(gs.cantabLimit)+1]
                gs.recycleLevel +=1
                self.tabLimitReached = False
                gui.debug('upping recycleLevel')




        #-----------------sell


        if(self.tabSellSelected or gs.tabInstaBuy==True):

            if(gs.scrapTabSplit!=0):
                gs.scrap    = round(((gs.scrapTabSplit/100) * gs.cantabs),2)
                gs.cantabs  = int((((100-gs.scrapTabSplit)/100)) * gs.cantabs)
                
            moneyEarned = gs.cantabs * gs.tabExchangeRate
            
            gs.money        += moneyEarned
            gs.totalCantabs += gs.cantabs
            gs.cantabs       = 0
            gs.money         = round(gs.money,2)

            me =  "{:.2f}".format(moneyEarned)
            if(gs.tabInstaBuy==False): desktop.overrideMessage = "Sold £ " + str(me)

            # TOdo display popup
            self.tabsSold = True

        if(self.tabsSold):

            notificationDisplayTime= self.notificationDisplayTime
            conditionsArray=[[gs.totalCantabs>19,gs.totalCantabs<42,'keep it up'],[gs.totalCantabs>45,gs.totalCantabs<65,'Half way there '],[gs.totalCantabs>80,gs.totalCantabs<100,'Almost done']]
            #Checks conditions and updates black notification box accordingly
            desktop.blackBoardOverride(conditionsArray,gui,gs)

            # ----------Alert notifications 
            sellCount = self.stopTimer.stopWatch(1,'Caps sold',desktop.overrideMessage,gs)
            
            if(sellCount):
                self.tabsSold = False


























        if(self.activeSubWidget==1):
            # Only Run if widget selected
            if(gs.ACTIVEWIDGET=='recycleCenter'):

                lPairArray = [ ("Caps Price", '£ '+ '{:.2f}'.format(gs.capExchangeRate)),("Caps Collected", str(gs.totalCaps)),('AutoCap', str(gs.autoCap))]
                rPairArray = [("Limit", str(gs.capLimit)),('Level',str(gs.recycleLevel)),("Magnets",str(gs.magnets)),('scrap',str(gs.scrap)) ]
                winX,winY,winW,winH = self.drawWindow(gui,phone,gs,self.activeSubWidget,'Recycling Center','Can Pull Caps',lPairArray,rPairArray)

                # --------DIMENSIONS
                
                collX       = winX + 0.20*winW
                collY       = winY + 0.7*winH
                sellX       = collX
                sellY       = collY + 0.1*winH
                autoX       = collX   + 0.24*winW
                autoY       = collY + 0.1*winH
                magnetX     = collX   + 0.4*winW
                magnetY     = collY
                scrapX      = collX   + 0.42*winW
                scrapY      = collY + 0.1*winH



                #-----------INC WIDGET: COLLECT 

                if(gs.totalCaps<gs.capLimit):
                    cap = gs.capLimit - (gs.totalCaps + gs.bottleCaps)
                    inc = 1 + gs.magnets
                    
                    #value incremented 
                    gs.bottleCaps, endX, endY =  gui.incrementableWidget(collX,collY,'Picked up', gs.bottleCaps,inc=inc,cap=cap,userInput=gui.user_input.returnedKey,incrementKey='c',insta=gs.capInstaBuy,instaMessage='AutoBuy on')
                    # Sell button
                    self.capSellSelected      = drawSelectableImage(gui.bank[0],gui.bank[1],(sellX,sellY),gui,trim=False)

                # -----------------buyMagnets
                self.buyMagnets(magnetX,magnetY,gs,gui,desktop)
                # -------------scrap %
                gs.scrapCapSplit, endX, endY =  gui.incDecWidgetAbsolute(scrapX,scrapY,'Scrap %', gs.scrapCapSplit,inc=10,cap=100)
                # -----------------Auto
                if(drawSelectableImage(gui.auto[0],gui.auto[1],(autoX,autoY),gui)): gs.autoCapEnabled = True
        

                # ----- Continuously call DISABLE SELL
                if(self.capLimitReached):
                    self.capSellSelected                 = False
                    drawText(gui.screen,gui.nanoNokiaFont, "Current Limit Reached",collX,collY, colour=(50,50,50))
                

        # Call Every Round
        # Instabuy
        # ------------------BackgroundJobs
        gs.bottleCaps = self.autoCollect(gs.bottleCaps,gs.autoCapEnabled,gs,(gs.capLimit - (gs.totalCaps + gs.bottleCaps)),self.capStopTimer,delay=gs.autoCap,inc = (1 + gs.magnets))

        # ----- SET LIMIT REACHED FLAG ONCE ONLY

        if((gs.totalCaps>=gs.capLimit) and (self.capLimitReached==False)):
            # call once only
            self.capLimitReached         = True
            desktop.overrideMessage      = 'Limit reached'
            self.notificationDisplayTime = 6
            gs.capRestrictedDate     = gs.gameTime.copy()
            


        # ----- RESET ONE DAY LATER
        if(self.capLimitReached):
            # time passed 
            daysPassed = gs.gameTime['daysPassed'] - gs.capRestrictedDate['daysPassed']
            if(daysPassed>0):
                if(gs.capLimit<gs.capLimits[-1]):
                    gs.capLimit = gs.capLimits[gs.capLimits.index(gs.capLimit)+1]
                gs.recycleLevel +=1
                self.capLimitReached = False
                gui.debug('upping recycleLevel')




        #-----------------sell


        if(self.capSellSelected or gs.capInstaBuy==True):

            if(gs.scrapCapSplit!=0):
                gs.scrap    = (gs.scrapCapSplit/100) * gs.bottleCaps
                gs.bottleCaps  = (((100-gs.scrapCapSplit)/100)) * gs.bottleCaps
                
            moneyEarned = gs.bottleCaps * gs.capExchangeRate
            
            gs.money        += moneyEarned
            gs.totalCaps += gs.bottleCaps
            gs.bottleCaps       = 0
            gs.money         = round(gs.money,2)

            me =  "{:.2f}".format(moneyEarned)
            if(gs.capInstaBuy==False): desktop.overrideMessage = "Sold £ " + str(me)

            # TOdo display popup
            self.capsSold = True

        if(self.capsSold):

            notificationDisplayTime= self.notificationDisplayTime
            conditionsArray=[[gs.totalCaps>19,gs.totalCaps<42,'keep it up'],[gs.totalCaps>45,gs.totalCaps<65,'Half way there '],[gs.totalCaps>80,gs.totalCaps<100,'Almost done']]
            #Checks conditions and updates black notification box accordingly
            desktop.blackBoardOverride(conditionsArray,gui,gs)

            # ----------Alert notifications 
            sellCount = self.stopTimer.stopWatch(1,'Caps sold',desktop.overrideMessage,gs)
            
            if(sellCount):
                self.capsSold = False











