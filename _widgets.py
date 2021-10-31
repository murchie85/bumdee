import pygame
from _draw import *
from _utils import *



def showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Widget",bodyText="Widget textX",selectable=True,flashAlert=False):
    selected = False
    
    
    selected = drawSelectableImage(gui.widgetNode[0],gui.widgetNode[1],(widgetNodeX,widgetNodeY),gui,trim=False)
    
    if(flashAlert):
        gui.widgetAnim.animate(gui,'showWidgNode',[gui.widgetNode[0],gui.widgetNode[2]],(0,10,10),(widgetNodeX,widgetNodeY))

    widgetNodeW = gui.widgetNode[0].get_rect().w

    

    hovered,tw,th= drawText(gui.screen,gui.nanoNokiaFont, headerText, widgetNodeX,widgetNodeY+8, gui.greenD,center=widgetNodeW)
    drawText(gui.screen,gui.nanoNokiaFont, bodyText, widgetNodeX,widgetNodeY+37, gui.greenD,center=widgetNodeW)
    
    if(selectable==False): return(False)
    
    return(selected)





class junkCollection():
    def __init__(self):
        self.activeSubWidget        = 0
        self.totalSubWidgets        = 3


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


    def manageWidget(self,gui,phone,gs,fx,desktop,adargs=None):


        selected   = False 
        selectable = True

        # ----------Draw Pull Tab Widget 

        freeHorizontalWidth = gui.width - phone.mobileW - 100
        
        widgetNodeW = gui.widgetNode[0].get_rect().w
        widgetNodeX = phone.mobilex + phone.mobileW + 0.5* widgetNodeW
        widgetNodeY = phone.mobiley + 50
        
        #-------------only one widget at a time
        # ------------If a widget is active disable all others
        if(gs.ACTIVEWIDGET!=None): selectable = False 
        
        selected = showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Pull Tab",bodyText="Tabs Collected: " + str(gs.totalCantabs),selectable=selectable)

        if(adargs=='demoWidgetAlert'):
            showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Pull Tab",bodyText="Tabs Collected: " + str(gs.cantabs),selectable=False,flashAlert=True)
            return()


        if(selected): gs.ACTIVEWIDGET = 'recycleCenter'

        self.recycleCenter(gui,gs,fx,desktop,phone)

        

    def drawWindow(self,gui,phone,gs,tabNo,h1,h2,lPairArray,rPairArray):
        winX        = phone.mobilex + phone.mobileW + 0.05*gui.width
        winY        = phone.mobiley 
        winH,winW   = gui.mechBoxMed[0].get_rect().h,gui.mechBoxMed[0].get_rect().w
        exitX       = winX + 0.92*winW
        exitY       = winY + 0.03*winH
        hedx        = winX + 0.6*winH
        hedy        = winY + 0.02*winH
        cptx        = winX + 0.18*winW
        cpty        = winY + 0.11*winH
        tbspx       = winX + 0.20*winW
        tbspy       = winY + 0.25*winH
        tbscy       = winY + 0.40*winH
        lineColour  = (45,113,70)
        LeftXMargin = winX+0.2*winW

        # --------draw gui

        drawSelectableImage(gui.mechBoxMedDark[tabNo],gui.mechBoxMedDark[tabNo],(winX,winY),gui)


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
        if(((gui.mouseCollides((gui.mx,gui.my),winX,winY,winW,winH)) == False) and gui.clicked):
            gs.ACTIVEWIDGET = None

        # ---------Exit Window
        if(gui.mouseCollides((gui.mx,gui.my),exitX,exitY,40,40)):
            exitSelected = drawSelectableImage(gui.mechBoxMedDark[-1],gui.mechBoxMedDark[-1],(winX,winY),gui)
            if(exitSelected):
                gs.ACTIVEWIDGET = None

        return(winX,winY,winW,winH)

    

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
                    value = value + inc

        return(value)


    
    def recycleCenter(self,gui,gs,fx,desktop,phone):



        if(self.activeSubWidget==0):
            # Only Run if widget selected
            if(gs.ACTIVEWIDGET=='recycleCenter'):
                c = fx.fadeOut(gui,inc=40,alpha=100)

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
                scrapX      = collX   + 0.42*winW
                scrapY      = collY + 0.1*winH



                #-----------INC WIDGET: COLLECT 

                if(gs.totalCantabs<gs.cantabLimit):
                    cap = gs.cantabLimit - (gs.totalCantabs + gs.cantabs)
                    inc = 1 + gs.magnets
                    
                    #value incremented 
                    gs.cantabs, endX, endY =  gui.incrementableWidget(collX,collY,'Picked up', gs.cantabs,inc=inc,cap=cap,userInput=gui.user_input.returnedKey,incrementKey='c')
                    # Sell button
                    self.tabSellSelected   = drawSelectableImage(gui.bank[0],gui.bank[1],(sellX,sellY),gui,trim=False)

                # -----------------buyMagnets
                self.buyMagnets(magnetX,magnetY,gs,gui,desktop)
                # -------------scrap %
                gs.scrapTabSplit, endX, endY =  gui.incDecWidgetAbsolute(scrapX,scrapY,'Scrap %', gs.scrapTabSplit,inc=10,cap=100)
                # -----------------Auto
                if(drawSelectableImage(gui.auto[0],gui.auto[1],(autoX,autoY),gui)): gs.autoTabEnabled = True
        

                # ----- Continuously call DISABLE SELL
                if(self.tabLimitReached):
                    self.tabSellSelected                 = False
                    drawText(gui.screen,gui.nanoNokiaFont, "Current Limit Reached",collX,collY, colour=(50,50,50))
                

        # Call Every Round

        if(gs.tabInstaBuy==True): self.tabSellSelected = True
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


        if(self.tabSellSelected):

            if(gs.scrapTabSplit!=0):
                gs.scrap    = (gs.scrapTabSplit/100) * gs.cantabs
                gs.cantabs  = (((100-gs.scrapTabSplit)/100)) * gs.cantabs
                
            moneyEarned = gs.cantabs * gs.tabExchangeRate
            
            gs.money        += moneyEarned
            gs.totalCantabs += gs.cantabs
            gs.cantabs       = 0
            gs.money         = round(gs.money,2)

            me =  "{:.2f}".format(moneyEarned)
            if(gs.autoTabEnabled==False): desktop.overrideMessage = "Sold £ " + str(me)

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
                c = fx.fadeOut(gui,inc=40,alpha=100)

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
                    gs.bottleCaps, endX, endY =  gui.incrementableWidget(collX,collY,'Picked up', gs.bottleCaps,inc=inc,cap=cap,userInput=gui.user_input.returnedKey,incrementKey='c')
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
        if(gs.capInstaBuy==True): self.capSellSelected = True
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


        if(self.capSellSelected):

            if(gs.scrapCapSplit!=0):
                gs.scrap    = (gs.scrapCapSplit/100) * gs.bottleCaps
                gs.bottleCaps  = (((100-gs.scrapCapSplit)/100)) * gs.bottleCaps
                
            moneyEarned = gs.bottleCaps * gs.capExchangeRate
            
            gs.money        += moneyEarned
            gs.totalCaps += gs.bottleCaps
            gs.bottleCaps       = 0
            gs.money         = round(gs.money,2)

            me =  "{:.2f}".format(moneyEarned)
            if(gs.autoCapEnabled==False): desktop.overrideMessage = "Sold £ " + str(me)

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


































        if(self.activeSubWidget==2):

            sellSelected = False 
            
            lPairArray = [ ("Tabs Price", '£ '+ '{:.2f}'.format(gs.canExchangeRate)),("Tabs Collected", str(gs.totalCans)),('AutoCan', str(gs.autoCan))]
            rPairArray = [("Limit", str(gs.canLimit)),('Level',str(gs.recycleLevel))]
            winX,winY,winW,winH = self.drawWindow(gui,phone,gs,self.activeSubWidget,'Recycling Center','Drink Cans',lPairArray,rPairArray)

            # --------DIMENSIONS
            
            collX       = winX + 0.20*winW
            collY       = winY + 0.7*winH
            sellX       = collX
            sellY       = collY + 0.1*winH
            magnetX     = collX   + 0.5*winW
            magnetY     = collY



            #-----------INC WIDGET: COLLECT 

            if(gs.totalCans<gs.canLimit):
                cap = gs.canLimit - (gs.totalCans + gs.cans)
                
                #value incremented 
                gs.cans, endX, endY =  gui.incrementableWidget(collX,collY,'Picked up', gs.cans,cap=cap,userInput=gui.user_input.returnedKey,incrementKey='c')
                # Sell button
                sellSelected           = drawSelectableImage(gui.bank[0],gui.bank[1],(sellX,sellY),gui,trim=False)
            


            # ----- SET LIMIT REACHED FLAG ONCE ONLY

            if((gs.totalCans>=gs.canLimit) and (self.canLimitReached==False)):
                # call once only
                self.canLimitReached = True
                desktop.overrideMessage      = 'Limit reached'
                gs.canRestrictedDate         = gs.gameTime.copy()


            # ----- COntinuously call DISABLE SELL
            if(self.canLimitReached):
                sellSelected                 = False
                drawText(gui.screen,gui.nanoNokiaFont, "Current Limit Reached",collX,collY, colour=(50,50,50))
            

            # ----- RESET ONE DAY LATER
            if(self.canLimitReached):
                # time passed 
                daysPassed = gs.gameTime['daysPassed'] - gs.canRestrictedDate['daysPassed']
                if(daysPassed>0):
                    if(gs.canLimit<gs.canLimits[-1]):
                        gs.canLimit = gs.canLimits[gs.canLimits.index(gs.canLimit)+1]
                    gs.recycleLevel +=1
                    self.canLimitReached = False
                    gui.debug('upping recycleLevel')




            #-----------------sell

            if(sellSelected):
                moneyEarned = gs.cans * gs.canExchangeRate
                
                gs.money        += moneyEarned
                gs.totalCans += gs.cans
                gs.cans    = 0
                gs.money         = round(gs.money,2)

                me =  "{:.2f}".format(moneyEarned)
                desktop.overrideMessage = "Sold £ " + str(me)

                # TOdo display popup
                self.cansSold = True

            if(self.cansSold):

                notificationDisplayTime= self.notificationDisplayTime
                conditionsArray=[[gs.totalCans>19,gs.totalCans<42,'keep it up'],[gs.totalCans>45,gs.totalCans<65,'Half way there '],[gs.totalCans>80,gs.totalCans<100,'Almost done']]
                #Checks conditions and updates black notification box accordingly
                desktop.blackBoardOverride(conditionsArray,gui,gs)

                # ----------Alert notifications
                sellCount = self.stopTimer.stopWatch(1,'Caps sold',desktop.overrideMessage,gs)
                
                if(sellCount):
                    self.cansSold = False
