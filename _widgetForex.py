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





class forex():
    def __init__(self):
        self.activeSubWidget        = 0
        self.totalSubWidgets        = 3


        self.notificationDisplayTime = 2
        self.stopTimer               =  stopTimer()


    def manageWidget(self,gui,phone,gs,fx,desktop,adargs=None):


        selected   = False 
        selectable = True

        # ----------Draw Pull Tab Widget 

        freeHorizontalWidth = gui.width - phone.mobileW - 100
        
        widgetNodeW = gui.widgetNode[0].get_rect().w
        widgetNodeX = phone.mobilex + phone.mobileW + 1.7* widgetNodeW
        widgetNodeY = phone.mobiley + 50
        
        #-------------only one widget at a time
        # ------------If a widget is active disable all others
        if(gs.ACTIVEWIDGET!=None): selectable = False 
        
        selected = showWidgNode(gui,widgetNodeX,widgetNodeY,headerText="Forex Exchange",bodyText="Profit: + £1.02",selectable=selectable)


        if(selected): gs.ACTIVEWIDGET = 'forexWidget'

        self.forexExchange(gui,gs,fx,desktop,phone)

        

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

    


    
    def forexExchange(self,gui,gs,fx,desktop,phone):

        print('recycleCenter Widget')