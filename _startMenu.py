from _draw       import *
from _effects    import *

def manageStartMenu(gui,gs,animateImgs,fx,introSlides,user_input,clicked,dialogue):
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
        ext = gui.exitButton.display(gui)
        if(ext and clicked): gs.running = False

        choices = ['Start Game', 'Continue', 'Options','debug','Exit']
        hovered = drawVerticleList(choices,gui.font,0.45*gui.width,0.35*gui.height,gui,(255, 255, 255))

        if(hovered and clicked):
            if(hovered=='Start Game'): gs.tempState = 'startGame'
            if(hovered=='Exit'): gs.running = False
            if(hovered=='debug'): gs.state = 'debug'
        
        if(gs.tempState=='startGame'):
            c = fx.fadeOut(gui)
            if(c): 
                gs.state     = 'begin'
                gs.tempState ='name'
                user_input.enteredString = gs.userName
                user_input.inputLimit = 10

    if(gs.state == 'debug'):
        drawImage(gui.screen,gui.menuBG,(0,0))
        fx.hurt(gs.state,gui)





    if(gs.state == 'begin'):
        
        gui.border(gui.themeColour)
        ext = gui.exitButton.display(gui)
        if(ext and clicked): gs.running = False

        fi = fx.fadeIn(gui)

        if(fi):
            text = "What is your name?"
            text = text.upper()
            
            if(gs.tempState=='name'):
                r = dialogue.drawDialogue(gui,gui.font, text,clicked, colour=(180, 180, 180))
                if(r):
                    user_input.processInput()
                    user_input.drawTextInput(user_input.enteredString,0.42*gui.width,0.35*gui.height)
                    if(user_input.returnedKey=='complete'):
                        gs.tempState ='nameComplete'
                        gs.userName  = user_input.enteredString

            if(gs.tempState=='nameComplete'):
                text = "Your name is " + str(gs.userName)
                nc = dialogue.drawDialogue(gui,gui.font, text,clicked, colour=(180, 180, 180))
                if(nc):
                    gs.counter -=1
                    if(gs.counter<1):
                        gs.counter = gs.initCounter
                        gs.tempState='gay'
                        user_input.enteredString = "Yes"

            if(gs.tempState=='gay'):
                gi = fx.fadeIn(gui)
                if(gi):
                    g = dialogue.drawDialogue(gui,gui.font,'Are you gay?',clicked, colour=(180, 180, 180))
                    if(g):
                        user_input.processInput()
                        user_input.drawTextInput(user_input.enteredString,0.42*gui.width,0.35*gui.height)
                        if(user_input.returnedKey=='complete'):
                            gs.tempState='gayAnswered'
                            gs.counter = 60
                        
            if(gs.tempState=='gayAnswered'):
                dialogue.drawDialogue(gui,gui.font,'Are you gay?',clicked, colour=(180, 180, 180))
                gs.counter -=1
                user_input.enteredString = 'Yes'
                user_input.drawTextInput(user_input.enteredString,0.42*gui.width,0.35*gui.height)
                if(gs.counter<1):
                    gs.counter = 50
                    gs.tempState='gayresponse'

            
            if(gs.tempState=='gayresponse'):
                text = "Thanks for coming out of the closet."
                ag = dialogue.drawDialogue(gui,gui.font, text,clicked, colour=(180, 180, 180))
                if(ag):
                    gs.counter -=1
                    if(gs.counter<1):
                        gs.counter   = gs.initCounter
                        gs.state     ='start'
                        gs.tempState = ""




    if(gs.state == 'start'):
        gui.border(gui.themeColour)
        ext = gui.exitButton.display(gui)
        if(ext and clicked): gs.running = False
        fi = fx.fadeIn(gui)

        text = "Three billion human lives ended on August 29, 1997. The survivors of the nuclear fire called the war Judgment Day. They lived only to face a new nightmare: the war against the Machines. The computer which controlled the machines, Skynet, sent two Terminators back through time. Their mission: to destroy the leader of the human Resistance, John Connor, my son. The first Terminator was programmed to strike at me, in the year 1984, before John was born. It failed. The second was sent to strike at John himself, when he was still a child. As before, the Resistance was able to send a lone warrior, a protector for John. It was just a question of which one of them would reach him first."
        st = dialogue.drawDialogue(gui,gui.font, text,clicked, colour=(180, 180, 180))

