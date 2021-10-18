
def gameLoop(gui,gs,animateImgs,fx,introSlides,user_input):
	if(gs.state == 'main'):
	    #init
	    gui.drawPhone('off')
	    gui.semiBorder()
	    # phone 
	    ext = gui.exitButton.display(gui)
	    if(ext and gui.clicked): gs.running = False