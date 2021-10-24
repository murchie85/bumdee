import pygame
from _draw import *



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


def bank(gs,desktop):
    moneyEarned = gs.cantabs * gs.exchangeRate
    
    gs.money        += moneyEarned
    gs.totalCantabs += gs.cantabs
    gs.cantabs       = 0
    gs.money         = round(gs.money,2)

    me =  "{:.2f}".format(moneyEarned)
    desktop.overrideMessage = "Banked £ " + str(me)

    # TOdo display popup




class junkCollection():
    def __init__(self):
        self.banked                  = False
        self.limitMessage            = False 
        self.notificationDisplayTime = 2

    def pullTab(self,gui,phone,gs,fx,desktop,adargs=None):

        selected   = False 
        selectable = True

        # ----------Draw Pull Tab Widget 

        freeHorizontalWidth = gui.width - phone.mobileW - 100
        
        widgetNodeW = gui.widgetNode[0].get_rect().w
        widgetNodeX = phone.mobilex + phone.mobileW + 0.5* widgetNodeW
        widgetNodeY = phone.mobiley + 50
        
        # If a widget is active disable all others
        if(gs.activeWidget!=None): selectable = False 
        
        selected = showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Pull Tab",bodyText="Tabs Collected: " + str(gs.totalCantabs),selectable=selectable)

        if(adargs=='demoWidgetAlert'):
            showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Pull Tab",bodyText="Tabs Collected: " + str(gs.cantabs),selectable=False,flashAlert=True)
            return()


        if(selected): gs.activeWidget = 'pullTab'

        


        #----------------BIG WINDOW    ***********



        if(gs.activeWidget=='pullTab'):
            
            bankSelected = False 
            c = fx.fadeOut(gui,inc=40,alpha=100)

            # --------DIMENSIONS
            windowX    = widgetNodeX
            windowY    = widgetNodeY
            winHeight,winWidth = gui.medActiveWidget.get_rect().h,gui.medActiveWidget.get_rect().w
            labelX    = windowX + 0.5*(winWidth-gui.medActiveWidgetLab.get_rect().w)
            labelY    = windowY-1.5*(gui.medActiveWidgetLab.get_rect().h)
            rCX       = labelX + 40
            rcY       = labelY+10
            cptx      = windowX + 0.20*winWidth
            cpty      = windowY + 0.10*winHeight
            tbscx     = windowX + 0.15*winWidth
            tbscy     = windowY + 0.20*winHeight
            collX     = windowX + 0.15*winWidth
            collY     = windowY + 0.5*winHeight
            bankX     = windowX + 0.15*winWidth
            bankY     = windowY + 0.6*winHeight

            exitX     = windowX + 0.92*winWidth
            exitY     = windowY + 0.03*winHeight


            # draw screen window
            drawImage(gui.screen, gui.medActiveWidget,(windowX,windowY))
            drawImage(gui.screen,gui.medActiveWidgetLab,(labelX,labelY))

            LeftXMargin = windowX+0.2*winWidth
            # ----------Heading 
            drawText(gui.screen,gui.nanoNokiaFont, 'Recycling Center',rCX,rcY, colour=(255, 255, 255))
            drawText(gui.screen,gui.nanoNokiaFont, 'Can Pull Tabs',cptx,cpty, colour=(255, 255, 255))

            
            # --------- TEXT : TABS COLLECTED
            hov, w,h = drawTextandBox(gui.screen,gui.nanoNokiaFont,tbscx,tbscy, "Tabs Collected", str(gs.totalCantabs))
            
            #-----------INC WIDGET: COLLECT 

            if(gs.totalCantabs<gs.cantabLimit):
                cap = gs.cantabLimit - (gs.totalCantabs + gs.cantabs)
                gs.cantabs, endX, endY =  gui.incrementableWidget(collX,collY,'Picked up', gs.cantabs,cap=cap)
                bankSelected = drawSelectableImage(gui.bank[0],gui.bank[1],(bankX,bankY),gui,trim=False)
            else:
                # -----------limit reached

                if(self.limitMessage==False):
                    bankSelected                 = False
                    desktop.overrideMessage      = 'Limit reached'
                    self.notificationDisplayTime = 6
                    self.limitMessage            = True

            # ---------TEMP LIMIT DISPLAY
            if(self.limitMessage):
                drawText(gui.screen,gui.nanoNokiaFont, "Current Limit Reached",collX,collY, colour=(50,50,50))





            #-----------BANK

            if(bankSelected):
                bank(gs,desktop)
                self.banked = True

            if(self.banked):

                notificationDisplayTime= self.notificationDisplayTime
                

                # motivation
                if(gs.totalCantabs>19 and gs.totalCantabs<22 ):
                    desktop.overrideMessage = 'keep it up'
                    notificationDisplayTime=4

                desktop.blackInfoBox(gui,gs,desktop.overrideMessage,notificationDisplayTime=notificationDisplayTime)


                bankCount = gs.stopWatch(1,'banked',desktop.overrideMessage)
                
                if(bankCount):
                    self.banked = False



            # exit box
            selected = drawSelectableImage(gui.minis[8],gui.minis[9],(exitX,exitY),gui,trim=False)
            if(selected):
                gs.activeWidget = None

