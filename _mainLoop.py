from _desktopFunctions  import *


def gameLoop(gui,gs,phone,desktop,animateImgs,fx,introSlides,user_input):
    if(gs.state == 'main'):
        

        #-----core functions


        desktop.drawDesktop(gui,gs,animateImgs,phone)
        phone.phoneMenu(gui,gs)
        gs.tickTime()
        

        # --------pull tab widget
        pullTab(gui,phone,gs,fx,desktop)



        # if alert, then phone needs to be drawn last
        if(phone.alert): phone.phoneMenu(gui,gs)

        # ---------Desktop buttons

        gui.exitButton.textColour, gui.themeColour = (0,128,0),(0,128,0)
        ext = gui.exitButton.displayCircle(gui)
        if(ext and gui.clicked): gs.running = False