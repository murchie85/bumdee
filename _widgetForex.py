import pygame
from _draw import *
from _utils import *
import random





class forex():
    def __init__(self,w,x,y):
        self.w                      = w
        self.x                      = x
        self.y                      = y

        self.activeSubWidget        = 0
        self.totalSubWidgets        = 3

        self.notificationDisplayTime = 2
        self.stopTimer               =  stopTimer()


        # -------investments 
        self.invested               = 'init'
        self.investedDate           = None
        self.investedDuration       = 0
        self.investedPair           = None
        self.initialRate            = None
        self.investedPercent        = 0
        self.investedAmount         = 0
        self.change                 = 0
        self.returnProfit           = 0
        

        self.forexObject            = {
                                       'GBP_USD':{'price':1.37,'base':1.37,'history':[1.37],'name':'GBP_USD'},
                                       'GBP_EUR':{'price':1.18,'base':1.18,'history':[1.18],'name':'GBP_EUR'}
                                       }
    def reset(self):
        self.invested               = 'no'
        self.investedDate           = None
        self.investedDuration       = 0
        self.investedPair           = None
        self.initialRate            = None
        self.investedPercent        = 0
        self.investedAmount         = 0
        self.change                 = 0
        self.returnProfit           = 0
  

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

    

    def invest(self,percent,pair,duration,gs,desktop):
        # -----------Make investment
        if(self.invested=='init'):
            self.investedPair    = self.forexObject[pair]
            self.initialRate     = self.investedPair['price']
            self.investedPercent = percent/100
            self.investedAmount  = self.investedPercent * gs.money
            self.returnProfit    = self.investedAmount
            
            # -------if too low
            if(self.investedAmount < 1):
                print('sorry not enough funds')
                return

            print('investedPair '    + str(self.investedPair['name']))
            print('initialRate '     + str(self.initialRate))
            print('investedPercent ' + str(self.investedPercent))
            print('investedAmount  ' + str(self.investedAmount))
            print(' ')
            desktop.overrideMessage = 'Invested £ ' + str(round(self.investedAmount,2))
            gs.money -= self.investedAmount
            self.investedDate     = gs.gameTime.copy()
            self.investedDuration = duration
            self.invested='investing'

    def forexTick(self,gs,desktop):
        """
        Todo appreciate base over time 
        """

        for pair in self.forexObject:
            currentPair = self.forexObject[pair]
            inc = (random.randrange(0,20)/100) *currentPair['price']
            choice = random.choice(['add','add','minus','same','same','same'])
            # regress to mean
            if(currentPair['price'] > 2.5*currentPair['base']): choice = random.choice(['add','minus','minus','minus','minus','minus','same','same','same','same','add'])
            if(currentPair['price'] < 0.2*currentPair['base']): choice = random.choice(['minus','add','add','add','add','add','same','same','same','same','minus'])
            
            if(choice=='add'):   currentPair['price'] += inc
            if(choice=='minus'): currentPair['price'] -= inc
            if(choice=='same'):  currentPair['price']  = currentPair['price']
            currentPair['price'] = round(currentPair['price'],2)
            currentPair['history'].append(currentPair['price'])
            
            if(self.invested=='investing'):
                if(self.investedPair['name']==pair):
                    daysPassed = gs.gameTime['daysPassed'] - self.investedDate['daysPassed']
                    if(daysPassed>self.investedDuration):
                        self.change = (currentPair['price'] - self.initialRate)
                        self.returnProfit = round(((self.change)*self.investedAmount),2)
                        # return investment + profits
                        desktop.overrideMessage = str('Profit made £ ' + str(round(self.returnProfit,2)))
                        gs.money += self.investedAmount + self.returnProfit
                        print('Current Pair: ' + str(pair))
                        print('Rate ' + str(currentPair['price']))
                        print('Change ' + str(self.change))
                        print('Profit ' + str(self.returnProfit))
                        print('Hist ' + str(currentPair['history'][-10:]))
                        print('')
                        self.reset()

    
    def forexExchange(self,gui,gs,fx,desktop,phone):

        self.invest(50,'GBP_USD',2,gs,desktop)
        
        # -----------tick stocks
        countdown = gs.countDownReal(3)
        if(countdown):
            self.forexTick(gs,desktop)

