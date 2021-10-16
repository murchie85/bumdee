import pygame
class gui():
    def __init__(self,white, screen, width, height,font,bigFont,smallFont,themeColour,exitButton):
        self.white         = white
        self.screen        = screen
        self.width         = width
        self.height        = height
        self.font          = font
        self.bigFont       = bigFont
        self.smallFont     = smallFont
        self.themeColour   = themeColour
        self.exitButton    = exitButton


        self.mx     = 0
        self.my     = 0


        self.menuBG = None

    def border(self,colour=(128,0,0)):
        rect = pygame.draw.rect(self.screen, colour, [0.1*self.width, 0.1*self.height, 0.8*self.width, 0.8*self.height],4)

