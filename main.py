import pygame
import os
import time
import math
import random
import json
import os
import os, sys

from _input                 import *
from _draw                  import *
from _fx                    import *
from _gui                   import *
from _gameState             import *
from _startMenu             import *
from _button                import *
from _music                 import *
from _phone                 import *
from _desktopFunctions      import *
from _storyFlow             import *
from _events                import *
from _widgetController      import *
from _widgetRecycle         import * 
from _widgetForex           import * 


# -----------VARIABLES & FLAGS

white          = (255,255,255)
green          = (0,255,0)
blue           = (176,224,230)
FPS            = 90
width, height  = 1500 ,850
themeColour    = (128,0,0)
time = 0
gs        = gameState('main')
gameFlow  = gameFlow()
#gs.tempState='startGame'

# ---------------PYGAME

pygame.init()
pygame.display.set_caption("Bumdonian")
clock          = pygame.time.Clock()
nextFrame      = pygame.time.get_ticks()
screen         = pygame.display.set_mode((width,height),pygame.DOUBLEBUF)
#phoneScreen    = pygame.display.set_mode((405,544),pygame.DOUBLEBUF)

pygame.time.set_timer(pygame.USEREVENT, 20)
font        = pygame.font.Font(None, 25)
font        = pygame.font.Font(None, 26)
bigFont     = pygame.font.Font(None, 32)
hugeNokiaFont  = pygame.font.Font('fonts/nokiafc22.ttf', 37)
smallNokiaFont = pygame.font.Font('fonts/nokiafc22.ttf', 18)
hugeFont       = pygame.font.Font('fonts/Orbitron-Regular.ttf', 40)
bigFont        = pygame.font.Font('fonts/Orbitron-Regular.ttf', 32)
font           = pygame.font.Font('fonts/Orbitron-Regular.ttf', 25)
smallFont      = pygame.font.Font('fonts/Orbitron-Regular.ttf', 20)
nanoFont       = pygame.font.Font('fonts/Orbitron-Regular.ttf', 14)


# ---------------CLASS OBJECTS

exitButton   = button(0.975*width,30,0,0,'x',themeColour,smallFont,textColour=themeColour)
nextButton   = button(0.475*width,0.8*height,0,0,'next',themeColour,smallFont,textColour=themeColour)



borderSlide         = pygame.image.load('pics/assets/backgrounds/border_static.png')

dialogue             = dialogue()
smsDialogue          = smsDialogue()
smsScrollDialogue    = smsScrollDialogue()
sDialogue            = scrollingDialogue()
music                = music()
gEvent               = processGameEvent()
notificationDialogue = notificationDialogue()
user_input           = userInputObject("","",(0.27,0.65,0.45,0.08), gui)

gui                   = gui(
                            white,
                            screen,
                            width,
                            height,
                            smallNokiaFont,
                            hugeNokiaFont,
                            font,bigFont,
                            hugeFont,
                            smallFont,
                            nanoFont,
                            themeColour,
                            exitButton,
                            nextButton,
                            dialogue,
                            sDialogue,
                            smsDialogue,
                            music,
                            borderSlide,
                            notificationDialogue,
                            user_input,
                            statusButton      = button(0.15*width,0.05*height,width/17,height/13,'ST',(0,128,0),hugeNokiaFont,textColour=(97,165,93)),
                            inventoryButton   = button(0.15*width,0.05*height,width/17,height/13,'£',(0,128,0),hugeNokiaFont,textColour=(97,165,93)),
                            noteButton        = button(0.15*width,0.05*height,width/17,height/13,'N',(0,128,0),hugeNokiaFont,textColour=(97,165,93)),
                            nokiaFont         = pygame.font.Font('fonts/nokiafc22.ttf', 25),
                            nanoNokiaFont     = pygame.font.Font('fonts/nokiafc22.ttf', 14),
                            smsFont           = pygame.font.Font('fonts/Orbitron-Regular.ttf', 22),
                            musicFont         = pygame.font.Font('fonts/Orbitron-Regular.ttf', 18),
                            jumboFont         = pygame.font.Font('fonts/Orbitron-Regular.ttf', 50),
                            gameTime          = 0,
                            smsScrollDialogue = smsScrollDialogue,
                            squareFont        = pygame.font.Font('fonts/FORCEDSQUARE.ttf', 28),
                            squareFontH       = pygame.font.Font('fonts/FORCEDSQUARE.ttf', 28),
                                                        
                            )



phone        = phone(gui.width,gui.height)
desktop      = desktop()
fx           = sfx(gui)
modifyInput  = manageInput()
animateImgs  = imageAnimate(0,10,10)
widgetAnim   = imageAnimate(0,10,10,name='WidgetAnimation')


# Adding to Gui
gui.fx              = fx
gui.animateImgs     = animateImgs
gui.widgetAnim      = widgetAnim

junkCollection       = junkCollection(gui.widgetNode[0].get_rect().w,phone.mobilex + phone.mobileW + (0.5* gui.widgetNode[0].get_rect().w),phone.mobiley + 50,phone.mobilex + phone.mobileW + 0.05*gui.width,phone.mobiley,gui.mechBoxMed[0].get_rect().h,gui.mechBoxMed[0].get_rect().w)
forexWidget          = forex(gui.widgetNode[0].get_rect().w,phone.mobilex + phone.mobileW + (1.7* gui.widgetNode[0].get_rect().w),phone.mobiley + 50)

gs.junk              = junkCollection
gs.forex             = forexWidget

# set up music

from os import listdir
from os.path import isfile, join
musicPath = 'music/'
musicFiles = [f for f in listdir(musicPath) if isfile(join(musicPath, f))]
gs.music = [[x,musicFiles[x],str(musicPath) + './' +str(musicFiles[x]) ] for x in range(0,len(musicFiles)) ]



# ****TurnDebug on/off***
gui.debugSwitch = False 

# ---------------setup finished

gs.itercount = 0
while gs.running:
    gs.itercount+=1

    screen.fill((0, 0, 0))
    gui.clicked = False
    # Reset the key each round
    user_input.returnedKey=''

    # Did the user click the window close button?
    for event in pygame.event.get():
        pos            = pygame.mouse.get_pos()
        if event.type == pygame.QUIT: gs.running = False
        if event.type == pygame.MOUSEBUTTONDOWN: gui.clicked  = True
        user_input = modifyInput.manageButtons(event,user_input,gs.state)

    
    gui.debug('gs.state: ' + str(gs.state) + ' gs.stage: ' + str(gs.stage) + ' gs.eventState : ' + str(gs.eventState ) + ' substate: ' + str(gameFlow.substate) +   ' gs.halt' + str(gs.halt) + ' dialogue state: ' + str(gui.smsScrollDialogue.finished) + ' cutscene: ' + str(gs.cutScene))
    gui.mx, gui.my = pygame.mouse.get_pos()


    # Manage Start Intro Loop
    #manageStartMenu(gui,gs,animateImgs,fx,user_input)



    # Archived Main Game Loops
    #gameLoop(gui,gs,gameFlow,phone,desktop,animateImgs,fx,user_input)

    if(gs.state == 'main'):
        

        #-----core functions

        commands = gameFlow.checkDecisionFlow(gs,gui,phone)

        for command in commands[0]: 
            if(command == 'desktop'):
                desktop.drawDesktop(gui,gs,animateImgs,phone)
           
            if(command == 'phone'):
                phone.phoneMenu(gui,gs)

            if(command == 'afterCommand'):
                gameFlow.checkDecisionFlow(gs,gui,phone,True)

        # --------pull tab widget
        widgetCoordinator(gui,phone,gs,fx,desktop,commands,commands[1])
        
        gEvent.processEvent(gs,gui)




        gs.tickTime()
        



        # ---------Desktop buttons
        if(gui.hideExitButton!=True):
            gui.exitButton.textColour, gui.themeColour = (0,128,0),(0,128,0)
            ext = gui.exitButton.displayCircle(gui)
            if(ext and gui.clicked): gs.running = False











    # Flip the display
    pygame.display.flip()
    # Tick
    gs.dt = clock.tick(FPS)
    gs.gameElapsed += gs.dt/1000
    #clock.tickck_busy_loop(120)
    continue

# Done! Time to quit.
pygame.quit()