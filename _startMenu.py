
def manageStartMenu(gs,gui,introSlides):
	"""runs function based on gamestate"""

    #---------------Title Screen

    if(gs.state == 'intro'):
        p,f = iterateImages(gui.screen,introSlides,p,f,s,(0,0))

        if(user_input.returnedKey == 'return'):
            user_input.returnedKey = ""
            gs.state = 'menu'


    #---------------Menu

    if(gs.state == 'menu'):
        drawImage(screen,menuBG,(0,0))
        choices = ['Start Game', 'Continue', 'Options','debug','Exit']

        hovered = drawVerticleList(choices,font,0.4*width,0.35*height,gui,(255, 255, 255))

        if(hovered and clicked):
            if(hovered=='Exit'): running = False
            if(hovered=='debug'): gs.state = 'debug'
    
    if(gs.state == 'debug'):
        drawImage(screen,menuBG,(0,0))
        fx.fadeIn(gs.state)


