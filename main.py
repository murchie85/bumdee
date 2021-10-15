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


# -----------VARIABLES & FLAGS

white      = (255,255,255)
green      = (0,255,0)
blue       = (176,224,230)
FPS            = 60
width, height  = 1500 ,850

time = 0
running = True
gs = gameState('intro')

# ---------------PYGAME

pygame.init()
pygame.display.set_caption("Bumdonian")
clock          = pygame.time.Clock()
nextFrame      = pygame.time.get_ticks()
screen   = pygame.display.set_mode((width,height), pygame.DOUBLEBUF)
pygame.time.set_timer(pygame.USEREVENT, 20)
font        = pygame.font.Font(None, 25)
font        = pygame.font.Font(None, 26)
bigFont     = pygame.font.Font(None, 32)
font        = pygame.font.Font('/Users/adammcmurchie/amu/amu_0.0.3/assets/font/Orbitron/static/Orbitron-Regular.ttf', 25)

# ---------------CLASS OBJECTS

gui = gui(white,screen,width,height,font)
fx  = sfx(gui)
introSlides = [pygame.image.load('pics/intro1.png'),pygame.image.load('pics/intro2.png')]
menuBG      = pygame.image.load('pics/intro3.png')
user_input   = userInputObject("","",(0.27,0.65,0.45,0.08), gui)
modifyInput  = manageInput()
animateImgs  = imageAnimate(0,10,10)







# ---------------setup finished


while running:

    screen.fill((0, 0, 0))
    clicked = False

    # Did the user click the window close button?
    for event in pygame.event.get():
        pos            = pygame.mouse.get_pos()
        if event.type == pygame.QUIT: running = False
        if event.type == pygame.MOUSEBUTTONDOWN: clicked  = True
        user_input = modifyInput.manageButtons(event,user_input,gs.state)

        
    gui.mx, gui.my = pygame.mouse.get_pos()



    #---------------Title Screen

    if(gs.state == 'intro'):
        animateImgs.animate(gui,gs.state,introSlides,(0,10,10),(0,0))

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








    #if(mouseInRec(mx, my, x, y, w, h) ): colColour = (255,255,255)
    #pygame.draw.rect(screen, blue, (20, 20, width - 20, height - 20),7,border_radius=1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
    


    # Flip the display
    pygame.display.flip()
    # Tick
    clock.tick(FPS)
    clock.tick_busy_loop(40)
    continue

# Done! Time to quit.
pygame.quit()