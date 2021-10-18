import pygame
import math

class button():
    ''''''
    def __init__(self, x,y, text,colour,font, thickness = 3,textColour=(200,200,200)):
        self.colour       = colour
        self.x            = x
        self.y            = y
        self.text         = text
        self.font         = font
        self.thickness    = thickness
        self.textColour   = textColour
        self.textsurface  = self.font.render(self.text, True, textColour)
        self.width        = self.textsurface.get_rect().width + 0.3*(self.textsurface.get_rect().width)
        self.height       = self.textsurface.get_rect().height + 0.1*(self.textsurface.get_rect().height)

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

    def display(self,gui,noBorder=False):
        textColour   = self.textColour
        borderColour = gui.themeColour
        hovered = self.isOver((gui.mx,gui.my))
        
        if(hovered): textColour = (100,100,100)
        if(hovered): borderColour = (100,100,100)

        textsurface    = self.font.render(self.text, True, textColour)

        gui.screen.blit(textsurface,(self.x,self.y))

        # Draw box
        if(noBorder): return(hovered)
        pygame.draw.rect(gui.screen,borderColour,[self.x -0.2*self.width ,self.y,self.width + 0.2*self.width,self.height], self.thickness)
        
        return(hovered)

    def displayCircle(self,gui,noBorder=False):
        textColour   = self.textColour
        borderColour = gui.themeColour
        hovered = self.isOver((gui.mx,gui.my))
        
        if(hovered): borderColour = (160,20,20)


        # Draw box
        if(noBorder): return(hovered)
        pygame.draw.circle(gui.screen, borderColour, (self.x,self.y+10), 10, 0)
        
        return(hovered)
