from _draw       import *
from _effects    import *

def manageStartMenu(gui,gs,animateImgs,fx,introSlides,user_input,clicked):
    """runs function based on gamestate"""

    #---------------Title Screen

    if(gs.state == 'intro'):
        
        animateImgs.animate(gui,gs.state,introSlides,(0,10,10),(0,0))

        if(user_input.returnedKey == 'return'):
            user_input.returnedKey = ""
            gs.state = 'menu'


    #---------------Menu

    if(gs.state == 'menu'):
        #drawImage(gui.screen,gui.menuBG,(0,0))
        gui.border(gui.themeColour)
        ext = gui.exitButton.display(gui,tx=3,ty=-2)

        choices = ['Start Game', 'Continue', 'Options','debug','Exit']

        hovered = drawVerticleList(choices,gui.font,0.45*gui.width,0.35*gui.height,gui,(255, 255, 255))

        if(hovered and clicked):
            if(hovered=='Start Game'): gs.state = 'begin'
            if(hovered=='Exit'): gs.running = False
            if(hovered=='debug'): gs.state = 'debug'
        if(ext and clicked): gs.running = False
    
    if(gs.state == 'debug'):
        drawImage(gui.screen,gui.menuBG,(0,0))
        fx.hurt(gs.state,gui)

