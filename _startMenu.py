from _draw           import *
from _fx             import *



def manageStartMenu(gui,gs,animateImgs,fx,user_input):
    """runs function based on gamestate"""

    #---------------Title Screen

    if(gs.state == 'intro'):
        
        animateImgs.animate(gui,gs.state,gui.titleScreenImgs,(0,10,10),(0,0))

        if(user_input.returnedKey == 'return'):
            user_input.returnedKey = ""
            gs.state = 'menu'


    #---------------Menu

    if(gs.state == 'menu'):
        #drawImage(gui.screen,gui.menuBG,(0,0))
        gui.border(gui.themeColour)
        ext = gui.exitButton.display(gui)
        if(ext and gui.clicked): gs.running = False

        choices = ['Start Game', 'Continue', 'Options','debug','Exit']
        hovered = drawVerticleList(choices,gui.font,0.45*gui.width,0.35*gui.height,gui,(255, 255, 255))

        if(hovered and gui.clicked):
            if(hovered=='Start Game'): gs.menuState = 'startGame'
            if(hovered=='Exit'): gs.running = False
            if(hovered=='debug'): gs.state = 'debug'
        
        if(gs.menuState=='startGame'):
            c = fx.fadeOut(gui)
            if(c): 
                gs.state     = 'begin'
                gs.menuState ='name'
                user_input.enteredString = gs.userName
                user_input.inputLimit = 10

    if(gs.state == 'debug'):
        drawImage(gui.screen,gui.menuBG,(0,0))
        gui.music.play("/Users/adammcmurchie/2021/Bumdonian/music/solitude.mp3",pos=54)

        #fx.hurt(gs.state,gui)






    if(gs.state == 'begin'):
        
        gui.border(gui.themeColour)
        ext = gui.exitButton.display(gui)
        if(ext and gui.clicked): gs.running = False

        if(gs.tempState=='name'): gs.userName = askQuestion("What is your name?",gs, gui,fx,user_input,returnValue='nameResponse',fade=True)
        if(gs.tempState=='nameResponse'): questionResponse(("Your name is " + str(gs.userName)),gs,gui,user_input,returnValue='gay',setCounterTime=20,setInputVal='Yes')
        if(gs.tempState=='gay'): askQuestion("Are you gay?",gs, gui,fx,user_input,'gayAnswered',True)
        
        if(gs.tempState=='gayAnswered'):
            if(gs.counter==None): gs.counter = 100
            gui.dialogue.drawDialogue(gui,gui.font,'Really?',gui.clicked, colour=(180, 180, 180),fade=False)
            gs.counter -=1
            user_input.enteredString = 'Yes'
            user_input.drawTextInput(user_input.enteredString,0.42*gui.width,0.35*gui.height)
            if(gs.counter<1):
                gs.counter = 50
                gs.tempState='gayresponse'

        if(gs.tempState=='gayresponse'): questionResponse( ('Thanks for coming out of the closet'),gs,gui,user_input,returnValue='startGame',setCounterTime=40,setInputVal='')
        if(gs.tempState=='startGame'): gs.state = 'start'


    if(gs.state == 'start'):
        #init
        gui.border(gui.themeColour)
        ext = gui.exitButton.display(gui)
        if(ext and gui.clicked): gs.running = False
        s = scrollingResponse((' '),("Starting Game...."),gs,gui,user_input,setCounterTime=40, sPos=(0.4*gui.width, 0.4*gui.height),delay=4)
        if(s):
            gs.state,gs.tempState = 'main',''






    if(gs.state == 'wake'):
        #init
        gui.border(gui.themeColour)
        ext = gui.exitButton.display(gui)
        if(ext and gui.clicked): gs.running = False

        if(gs.tempState=='sgs'):
            finished = scrollingResponse(('Unknown Person'),("Wake up cunt"),gs,gui,user_input,setCounterTime=40, titlePos=(gui.bx + 100,gui.by+70),delay=2)
            if(finished): gs.tempState = 'changecolour'
        if(gs.tempState=='changecolour'):
            gui.themeColour = (0,128,0)


