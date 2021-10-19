
def gameLoop(gui,gs,phone,desktop,animateImgs,fx,introSlides,user_input):
	if(gs.state == 'main'):
	    #init
	    
	    desktop.drawDesktop(gui,gs,animateImgs)
	    phone.drawPhone('off',gui)
	    


	    # phone 
	    gui.exitButton.textColour, gui.themeColour = (0,128,0),(0,128,0)
	    ext = gui.exitButton.displayCircle(gui)
	    if(ext and gui.clicked): gs.running = False