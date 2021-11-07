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
        self.totalSubWidgets        = 1
        self.chosenData             = []

        self.notificationDisplayTime = 2
        self.stopTimer               =  stopTimer()



    def reset(self,gs):
        gs.invested               = 'no'
        gs.investedDate           = None
        gs.investedDuration       = 0
        gs.investedPair           = None
        gs.initialRate            = None
        gs.investedPercent        = 0
        gs.investedAmount         = 0
        gs.change                 = 0
        gs.returnProfit           = 0
  

    def drawWindow(self,gui,phone,desktop,gs,tabNo,h1,h2,lPairArray=[],rPairArray=[]):
        winX        = phone.mobilex + phone.mobileW + 50
        winY        = 0.17*gui.height
        winH,winW   = gui.mechBoxBig[0].get_rect().h,gui.mechBoxBig[0].get_rect().w
        exitX       = winX + 0.96*winW
        exitY       = winY + 0.03*winH
        hedx        = winX + 0.6*winH
        hedy        = winY + 0.02*winH
        cptx        = winX + 0.18*winW
        cpty        = winY + 0.095*winH
        
        tbspx       = winX + 0.20*winW
        tbspy       = winY + 0.25*winH
        tbscy       = winY + 0.40*winH
        lineColour  = (45,113,70)
        LeftXMargin = winX+0.2*winW

        # --------draw gui

        drawSelectableImage(gui.mechBoxBig[tabNo],gui.mechBoxBig[tabNo],(winX,winY),gui)

        # ----------Heading 
        drawText(gui.screen,gui.squareFontH, h1,hedx,hedy, colour=(205, 230, 180))
        drawText(gui.screen,gui.squareFont, h2,cptx,cpty, colour=(205, 230, 180))
        

        # --------- draw pair butttons
        GU,x,y = drawTxtBtnAdvanced(gui.mechPlainBtnMed[0],gui.mechPlainBtnMed[1],(winX+0.12*winW,winY+0.65*winH),gui,'GBP_USD',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
        GE,x,y = drawTxtBtnAdvanced(gui.mechPlainBtnMed[0],gui.mechPlainBtnMed[1],(x,winY+0.65*winH),gui,'GBP_EUR',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
        GJ,x,y = drawTxtBtnAdvanced(gui.mechPlainBtnMed[0],gui.mechPlainBtnMed[1],(x,winY+0.65*winH),gui,'GBP_YEN',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
        UG,x1,y2 = drawTxtBtnAdvanced(gui.mechPlainBtnMed[0],gui.mechPlainBtnMed[1],(winX+0.12*winW,y+10),gui,'USD_GBP',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
        UE,x2,y2 = drawTxtBtnAdvanced(gui.mechPlainBtnMed[0],gui.mechPlainBtnMed[1],(x1            ,y+10),gui,'USD_EUR',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
        UJ,x3,y2 = drawTxtBtnAdvanced(gui.mechPlainBtnMed[0],gui.mechPlainBtnMed[1],(x2            ,y+10),gui,'USD_YEN',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
        
        if(self.chosenData==[]): self.chosenData = gs.forexObject['GBP_USD']['history']
        for xpair in [[GU,'GBP_USD'],[GE,'GBP_EUR'],[GJ,'GBP_YEN']]:
            if(xpair[0]):  
                gs.investedPair = gs.forexObject[xpair[1]]
                self.chosenData = gs.forexObject[xpair[1]]['history']

        # --------Draw graph
        stepGraph('Test Data',self.chosenData[-15:],200,winX+0.12*winW, winY+0.4*winH,25,gui.font,gui,points=15,colour=(0,150,0))

        
        # -------- draw invest button
        invest,xe,ye = drawTxtBtnAdvanced(gui.mechBtnMed[0],gui.mechBtnMed[1],(x+0.25*winW,winY+0.65*winH),gui,'Invest',font=gui.nanoNokiaFont,txtColour=(215,233,149),yadj=0.5)
        gs.investedDuration, endX, endY =  gui.incDecWidgetAbsolute(x+0.25*winW,ye+50,'Period:', gs.investedDuration,inc=1,cap=10)
        if(invest):
            if(gs.invested=='no' and gs.investedPair!=None):
                gs.invested='init'
            elif(gs.invested=='investing'):
                desktop.overrideMessage = 'Already Investing.'
            elif(gs.investedPair==None):
                desktop.overrideMessage = 'Please pick a currency pair.'
            else:
                desktop.overrideMessage = 'Cant invest at this time.'
        
        # ------- Change Widgets
        if(gui.user_input.returnedKey =='down'):
            self.activeSubWidget = self.activeSubWidget + 1
            gui.user_input.returnedKey =''
        if(gui.user_input.returnedKey =='up'):
            self.activeSubWidget = self.activeSubWidget - 1
            gui.user_input.returnedKey =''
        if(self.activeSubWidget>self.totalSubWidgets-1): self.activeSubWidget=0
        if(self.activeSubWidget<0): self.activeSubWidget=self.totalSubWidgets-1

        
        # -----------grid
        #xend,yend=drawTextandBoxGrid(gui.screen,gui.nanoNokiaFont,tbspx,tbspy, lPairArray,lineColour=(45,102,66))
        #drawTextandBoxGrid(gui.screen,gui.nanoNokiaFont,xend + 70,tbspy, rPairArray,lineColour=lineColour )
          


        # --------exit if clicked outside
        if(((gui.mouseCollides((gui.mx,gui.my),winX,winY,winW,winH)) == False) and gui.clicked):
            gs.ACTIVEWIDGET = None

        # ---------Exit Window
        if(gui.mouseCollides((gui.mx,gui.my),exitX,exitY,40,40)):
            exitSelected = drawSelectableImage(gui.mechBoxBig[-1],gui.mechBoxBig[-1],(winX,winY),gui)
            if(exitSelected):
                gs.ACTIVEWIDGET = None

        return(winX,winY,winW,winH)

    

    def invest(self,percent,pair,gs,desktop):
        # -----------Make investment
        if(gs.invested=='init' and gs.investedPair!=None):
            gs.initialRate     = gs.investedPair['price']
            gs.investedPercent = percent/100
            gs.investedAmount  = gs.investedPercent * gs.money
            gs.returnProfit    = gs.investedAmount
            
            # -------if too low
            if(gs.investedAmount < 1):
                print('sorry not enough funds')
                return

            print('investedPair '    + str(gs.investedPair['name']))
            print('initialRate '     + str(gs.initialRate))
            print('investedPercent ' + str(gs.investedPercent))
            print('investedAmount  ' + str(gs.investedAmount))
            print(' ')
            desktop.overrideMessage = 'Invested £ ' + str(round(gs.investedAmount,2))
            gs.money -= gs.investedAmount
            gs.investedDate     = gs.gameTime.copy()
            gs.invested='investing'

    def forexTick(self,gs,desktop):
        """
        Todo appreciate base over time 
        """

        for pair in gs.forexObject:
            currentPair = gs.forexObject[pair]
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
            
            if(gs.invested=='investing'):
                if(gs.investedPair['name']==pair):
                    daysPassed = gs.gameTime['daysPassed'] - gs.investedDate['daysPassed']
                    gs.change = (currentPair['price'] - gs.initialRate)
                    gs.returnProfit = round(((gs.change)*gs.investedAmount),2)
                    if(daysPassed>gs.investedDuration):
                        # return investment + profits
                        desktop.overrideMessage = str('Profit made £ ' + str(round(gs.returnProfit,2)))
                        gs.money += gs.investedAmount + gs.returnProfit
                        print('Current Pair: ' + str(pair))
                        print('Rate ' + str(currentPair['price']))
                        print('Change ' + str(gs.change))
                        print('Profit ' + str(gs.returnProfit))
                        print('Hist ' + str(currentPair['history'][-10:]))
                        print('')
                        self.reset(gs)

    
    def forexExchange(self,gui,gs,fx,desktop,phone):

        if(gs.ACTIVEWIDGET=='forexExchange'):

            #lPairArray = [ ("Tabs Price", '£ '+ '{:.2f}'.format(gs.tabExchangeRate)),("Tabs Collected", str(gs.totalCantabs)),('AutoTab', str(gs.autoTab))]
            #rPairArray = [("Limit", str(gs.cantabLimit)),('Level',str(gs.recycleLevel)),("Magnets",str(gs.magnets)),('scrap',str(gs.scrap)) ]
            winX,winY,winW,winH = self.drawWindow(gui,phone,desktop,gs,self.activeSubWidget,'Forex Exchange','Forex Control Panel',lPairArray=[],rPairArray=[])


        self.invest(50,'GBP_USD',gs,desktop)
        
        # -----------tick stocks
        countdown = gs.countDownReal(2)
        if(countdown):
            self.forexTick(gs,desktop)

