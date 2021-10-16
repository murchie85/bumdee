import pygame
import math

class button():
    ''''''
    def __init__(self, x,y,width,height, text,colour,font, thickness = 3,textColour=(200,200,200)):
        self.colour       = colour
        self.x            = x
        self.y            = y
        self.width        = width
        self.height       = height
        self.text         = text
        self.font         = font
        self.thickness    = thickness
        self.textColour   = textColour

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

    def display(self,gui,tx=0,ty=0):
        textColour   = self.textColour
        borderColour = gui.themeColour
        hovered = self.isOver((gui.mx,gui.my))
        
        if(hovered): textColour = (100,100,100)
        if(hovered): borderColour = (100,100,100)

        textsurface    = self.font.render(self.text, True, textColour)

        gui.screen.blit(textsurface,(self.x+tx,self.y+ty))

        # Draw box
        pygame.draw.rect(gui.screen,borderColour,[self.x,self.y,self.width,self.height], self.thickness)
        
        return(hovered)
