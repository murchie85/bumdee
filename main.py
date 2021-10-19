import pygame
import os
import time
import math
import random
import json
import os
import pandas as pd
import statistics
import os, sys

from _input      import *
from _draw       import *
from _effects    import *
from _gui        import *
from _gameState  import *
from _startMenu  import *
from _button     import *
from _music      import *
from _game       import *
from _phone      import *


# -----------VARIABLES & FLAGS

white          = (255,255,255)
green          = (0,255,0)
blue           = (176,224,230)
FPS            = 60
width, height  = 1500 ,850
themeColour    = (128,0,0)
time = 0
gs = gameState('main')
#gs.tempState='startGame'

# ---------------PYGAME

pygame.init()
pygame.display.set_caption("Bumdonian")
clock          = pygame.time.Clock()
nextFrame      = pygame.time.get_ticks()
screen   = pygame.display.set_mode((width,height),pygame.DOUBLEBUF)

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

statusButton    = button(0.15*width,0.05*height,width/17,height/13,'ST',(0,128,0),hugeNokiaFont,textColour=(97,165,93))
inventoryButton = button(0.15*width,0.05*height,width/17,height/13,'£',(0,128,0),hugeNokiaFont,textColour=(97,165,93))
noteButton      = button(0.15*width,0.05*height,width/17,height/13,'N',(0,128,0),hugeNokiaFont,textColour=(97,165,93))


borderSlides = [pygame.image.load('pics/frame/border1.png'),pygame.image.load('pics/frame/border2.png'),pygame.image.load('pics/frame/border3.png'),pygame.image.load('pics/frame/border4.png'),pygame.image.load('pics/frame/border5.png'),pygame.image.load('pics/frame/border6.png'),pygame.image.load('pics/frame/border7.png'),pygame.image.load('pics/frame/border8.png')]

dialogue     = dialogue()
smsDialogue  = smsDialogue()
sDialogue    = scrollingDialogue()
music        = music()

gui              = gui(white,screen,width,height,smallNokiaFont,hugeNokiaFont,font,bigFont,hugeFont,smallFont,nanoFont,themeColour,exitButton,nextButton,dialogue,sDialogue,smsDialogue,music,borderSlides)
gui.statusButton    = statusButton
gui.inventoryButton = inventoryButton
gui.noteButton      = noteButton

phone        = phone(gui.width,gui.height)
desktop      = desktop()
fx           = sfx(gui)
introSlides  = [pygame.image.load('pics/intro/intro1.png'),pygame.image.load('pics/intro/intro2.png')]
gui.menuBG   = pygame.image.load('pics/intro/intro3.png')
user_input   = userInputObject("","",(0.27,0.65,0.45,0.08), gui)
modifyInput  = manageInput()
animateImgs  = imageAnimate(0,10,10)








# ---------------setup finished


while gs.running:

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

        
    gui.mx, gui.my = pygame.mouse.get_pos()


    # Manage Start Intro Loop
    manageStartMenu(gui,gs,animateImgs,fx,introSlides,user_input)
    gameLoop(gui,gs,phone,desktop,animateImgs,fx,introSlides,user_input)


    # Flip the display
    pygame.display.flip()
    # Tick
    clock.tick(FPS)
    clock.tick_busy_loop(120)
    continue

# Done! Time to quit.
pygame.quit()