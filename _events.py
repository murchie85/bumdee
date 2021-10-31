from _draw import *
class processGameEvent():

    def __init__(self):
        self.eventState = None


    def processEvent(self,gs,gui):



        #----------NEXT DAY 
        if(gs.eventState == 'nextDay'):
            gs.hault = True
            gui.debug('Going to Next Day')
            gs.eventState = 'animateNextDay'
        if(gs.eventState=='animateNextDay'):
            c = gui.fx.boxOut(gui,'gs.stage',inc=15)
            gui.hideExitButton = True
            if(c):
                gs.eventState = 'dayReport'
                gui.debug('Day complete')
                gui.hideExitButton = False
                # One time set key
                gs.nextDay()

                


        if(gs.eventState == 'dayReport'):
            print('notifying day report')
            if(gs.notifyPlayer(str(str("Days Report: ") + str(gs.gameTime)))): gs.eventState = None
                
           

        # =========NOTIFICATION

        if(str(gs.notify).upper() == 'ACCEPT'):
            """
            To be called once only
            Use notify key to prevent duplication
            """

            # returns accept once complete
            gs.halt   = True
            windowX   = 0.3*gui.width
            windowY   = 0.15*gui.height
            winHeight,winWidth = gui.bigActiveWidget.get_rect().h,gui.bigActiveWidget.get_rect().w
            
            # Draw Screen Window
            drawImage(gui.screen, gui.bigActiveWidget,(windowX,windowY))

            # draw Dialogue
            x,y = windowX + 0.10 * winWidth, windowY + 0.20*winHeight
            drawText(gui.screen,gui.bigFont, "Notification",windowX,y - 0.1*winHeight, colour=gui.greenD,center=winWidth)
            gui.notificationDialogue.drawDialogue(gui,gui.font, gs.notifyMessage,(x,y),0.8*winWidth,0.45*winHeight,gui.clicked, gui.greenD, source=gs.notifyMessage)

            # Draw Button
            text='Accept'
            accept = drawTxtBtn(gui.notitfyBtnMed[1],gui.notitfyBtnMed[0],(windowX+0.4*winWidth,windowY + 0.8*winHeight),gui,text)
            if(accept): 
                gs.notify           = None  # has to be reset by caller
                gs.notifyState      = 'inactive'
                gs.halt             = False
