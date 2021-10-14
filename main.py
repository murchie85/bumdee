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

from _input import *
from _draw  import *

# ---------------classes

class gui():
    def __init__(self,white, screen, WIDTH, HEIGHT,font):
        self.white  = white
        self.screen = screen
        self.WIDTH  = WIDTH
        self.HEIGHT = HEIGHT
        self.font   = font


# ---------------setup
pygame.init()
pygame.display.set_caption("Bumdonian")
clock          = pygame.time.Clock()
nextFrame      = pygame.time.get_ticks()
FPS            = 60
WIDTH, HEIGHT  = 1500 ,850
screen   = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.time.set_timer(pygame.USEREVENT, 20)
white      = (255,255,255)
green      = (0,255,0)
blue       = (176,224,230)




font        = pygame.font.Font(None, 25)
font        = pygame.font.Font(None, 26)
bigFont     = pygame.font.Font(None, 32)
font        = pygame.font.Font('/Users/adammcmurchie/amu/amu_0.0.3/assets/font/Orbitron/static/Orbitron-Regular.ttf', 25)

gui = gui(white,screen,WIDTH,HEIGHT,font)

introSlides = [pygame.image.load('pics/intro1.png'),pygame.image.load('pics/intro2.png')]
menuBG      = pygame.image.load('pics/intro3.png')
p,f,s = 0,10,10
user_input   = userInputObject("","",(0.27,0.65,0.45,0.08), gui)
modifyInput  = manageInput()


# Flags 
time = 0
running = True
gameState = 'intro'




# ---------------setup finished


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        pos            = pygame.mouse.get_pos()
        if event.type == pygame.QUIT: running = False
        user_input = modifyInput.manageButtons(event,user_input,gameState)

        
    screen.fill((0, 0, 0))

    mx, my = pygame.mouse.get_pos()

    #pygame.draw.rect(screen, blue, (20, 20, WIDTH - 20, HEIGHT - 20),7,border_radius=1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
    
    # Title Screen 
    if(gameState == 'intro'):
        p,f = iterateImages(screen,introSlides,p,f,s,(0,0))

        if(user_input.returnedKey == 'return'):
            user_input.returnedKey = ""
            gameState = 'menu'

    if(gameState == 'menu'):
        drawImage(screen,menuBG,(0,0))

    








    #if(mouseInRec(mx, my, x, y, w, h) ): colColour = (255,255,255)


    
    




    # Flip the display
    pygame.display.flip()
    # Tick
    clock.tick(FPS)
    clock.tick_busy_loop(40)
    continue

# Done! Time to quit.
pygame.quit()