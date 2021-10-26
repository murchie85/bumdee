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


def sell(gs,desktop):
    moneyEarned = gs.cantabs * gs.exchangeRate
    
    gs.money        += moneyEarned
    gs.totalCantabs += gs.cantabs
    gs.cantabs       = 0
    gs.money         = round(gs.money,2)

    me =  "{:.2f}".format(moneyEarned)
    desktop.overrideMessage = "Sold £ " + str(me)

    # TOdo display popup




class junkCollection():
    def __init__(self):
        self.sold                  = False
        self.limitMessage            = False 
        self.notificationDisplayTime = 2
        self.stopTimer               =  stopTimer()

    def pullTab(self,gui,phone,gs,fx,desktop,adargs=None):

        selected   = False 
        selectable = True

        # ----------Draw Pull Tab Widget 

        freeHorizontalWidth = gui.width - phone.mobileW - 100
        
        widgetNodeW = gui.widgetNode[0].get_rect().w
        widgetNodeX = phone.mobilex + phone.mobileW + 0.5* widgetNodeW
        widgetNodeY = phone.mobiley + 50
        
        #-------------only one widget at a time
        # ------------If a widget is active disable all others
        if(gs.activeWidget!=None): selectable = False 
        
        selected = showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Pull Tab",bodyText="Tabs Collected: " + str(gs.totalCantabs),selectable=selectable)

        if(adargs=='demoWidgetAlert'):
            showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Pull Tab",bodyText="Tabs Collected: " + str(gs.cantabs),selectable=False,flashAlert=True)
            return()


        if(selected): gs.activeWidget = 'pullTab'

        


        #----------------BIG WINDOW    ***********



        if(gs.activeWidget=='pullTab'):
            
            sellSelected = False 
            c = fx.fadeOut(gui,inc=40,alpha=100)

            # --------DIMENSIONS
            windowX    = widgetNodeX
            windowY    = widgetNodeY
            winHeight,winWidth = gui.medActiveWidget.get_rect().h,gui.medActiveWidget.get_rect().w
            labelX    = windowX + 0.5*(winWidth-gui.medActiveWidgetLab.get_rect().w)
            labelY    = windowY-1.5*(gui.medActiveWidgetLab.get_rect().h)
            rCX       = labelX + 40
            rcY       = labelY+10
            cptx      = windowX + 0.37*winWidth
            cpty      = windowY + 0.10*winHeight
            tbspx     = windowX + 0.15*winWidth
            tbspy     = windowY + 0.25*winHeight
            tbscx     = tbspx
            tbscy     = windowY + 0.40*winHeight
            collX     = windowX + 0.15*winWidth
            collY     = windowY + 0.7*winHeight
            sellX     = collX   + 0.5*winWidth
            sellY     = collY

            exitX     = windowX + 0.92*winWidth
            exitY     = windowY + 0.03*winHeight


            # draw screen window
            drawImage(gui.screen, gui.medActiveWidget,(windowX,windowY))
            drawImage(gui.screen,gui.medActiveWidgetLab,(labelX,labelY))

            LeftXMargin = windowX+0.2*winWidth
            # ----------Heading 
            drawText(gui.screen,gui.nanoNokiaFont, 'Recycling Center',rCX,rcY, colour=(255, 255, 255))
            drawText(gui.screen,gui.nanoNokiaFont, 'Can Pull Tabs',cptx,cpty, colour=(255, 255, 255))

            # --------- TEXT : TAB Price
            pairArray = [ ("Tabs Price", '£ '+ '{:.2f}'.format(gs.exchangeRate)),("Tabs Collected", str(gs.totalCantabs))]
            xend,yend=drawTextandBoxGrid(gui.screen,gui.nanoNokiaFont,tbspx,tbspy, pairArray )
            pairArray = [("Limit", str(gs.cantabLimit)),('Level',str(gs.recycleLevel))]
            drawTextandBoxGrid(gui.screen,gui.nanoNokiaFont,xend + 30,tbspy, pairArray )
              




            # ----------Logic 




            #-----------INC WIDGET: COLLECT 

            if(gs.totalCantabs<gs.cantabLimit):
                cap = gs.cantabLimit - (gs.totalCantabs + gs.cantabs)
                #value incremented 
                gs.cantabs, endX, endY =  gui.incrementableWidget(collX,collY,'Picked up', gs.cantabs,cap=cap)
                # Sell button
                sellSelected           = drawSelectableImage(gui.sell[0],gui.sell[1],(sellX,sellY),gui,trim=False)
            


            # ----- if Cantab Limit Reached 
            if(gs.totalCantabs>=gs.cantabLimit): 
                # -----------limit reached

                if(self.limitMessage==False):
                    sellSelected                 = False
                    desktop.overrideMessage      = 'Limit reached'
                    self.notificationDisplayTime = 6
                    self.limitMessage            = True
                    gs.restrictionReached      = gs.gameTime.copy()



            # ---------TEMP LIMIT DISPLAY
            if(self.limitMessage):
                drawText(gui.screen,gui.nanoNokiaFont, "Current Limit Reached",collX,collY, colour=(50,50,50))

                # First Notification 
                if(gs.cantabLimit==gs.limits[0]):
                    gs.notify        = 'accept'
                    gs.notifyMessage = "Your have reached your limit, it will reset the following day. Note, not all limits reset the following day."
                    
            
                #----increment limit
                # time passed 
                daysPassed = gs.gameTime['daysPassed'] - gs.restrictionReached['daysPassed']
                if(daysPassed>0):
                    if(gs.cantabLimit<gs.limits[-1]):
                        gs.cantabLimit = gs.limits[gs.limits.index(gs.cantabLimit)+1]
                    self.limitMessage = False
                    gs.recycleLevel +=1
                    print('upping recycleLevel')

            # Unlock once accepted
            if(gs.notifyChoice=='accepted'): gs.notify = False


            #-----------------sell

            if(sellSelected):
                sell(gs,desktop)
                self.sold = True

            if(self.sold):

                notificationDisplayTime= self.notificationDisplayTime
                conditionsArray=[[gs.totalCantabs>19,gs.totalCantabs<42,'keep it up'],[gs.totalCantabs>45,gs.totalCantabs<65,'Half way there '],[gs.totalCantabs>80,gs.totalCantabs<100,'Almost done']]
                #Checks conditions and updates black notification box accordingly
                desktop.blackBoardOverride(conditionsArray,gui,gs)

                # ----------Alert notifications
                sellCount = self.stopTimer.stopWatch(1,'sold',desktop.overrideMessage,gs)
                
                if(sellCount):
                    self.sold = False






            # exit box
            selected = drawSelectableImage(gui.minis[8],gui.minis[9],(exitX,exitY),gui,trim=False)
            if(selected):
                gs.activeWidget = None

