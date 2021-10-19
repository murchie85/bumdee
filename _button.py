import pygame
import math

class button():
    ''''''
    def __init__(self, x,y,width,height,text,colour,font, thickness = 3,textColour=(200,200,200)):
        self.x            = x
        self.y            = y
        self.width        = width
        self.height       = height
        self.text         = text
        self.colour       = colour
        self.font         = font
        self.thickness    = thickness
        self.textColour   = textColour
        self.textsurface  = self.font.render(self.text, True, textColour)


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False

    def display(self,gui,noBorder=False,fillColour=None,updatePos=None,hoverBoxCol=None,hoverTextCol=None):
        
        if(updatePos):
            self.x,self.y = updatePos[0],updatePos[1]
        
        textColour   = self.textColour
        borderColour = gui.themeColour
        hovered = self.isOver((gui.mx,gui.my))

        if(hovered): 
            textColour = (100,100,100)
            if(hoverTextCol):
                textColour= hoverTextCol
        if(hovered): 
            borderColour = (100,100,100)
            if(hoverBoxCol):
                borderColour = hoverBoxCol

        textsurface    = self.font.render(self.text, True, textColour)
        tw = textsurface.get_rect().width
        th = textsurface.get_rect().height

        if(self.width==0): self.width = 1.3*tw
        if(self.height==0): self.height = 1.3*th

        

        # Draw box
        bx,by = self.x,self.y
        bw,bh = self.width,self.height

        if(fillColour):
            pygame.draw.rect(gui.screen,fillColour,[ bx,by,bw,bh],border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        if(noBorder): return(hovered,bw,bh)
        # draw Border
        pygame.draw.rect(gui.screen,borderColour,[bx,by,bw,bh], self.thickness,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # text at end
        gui.screen.blit(textsurface,(self.x + 0.5*(self.width-tw),self.y+ 0.5*(self.height-th)))


        return(hovered,bw,bh)

    def displayCircle(self,gui,noBorder=False):
        textColour   = self.textColour
        borderColour = gui.themeColour
        hovered = self.isOver((gui.mx,gui.my))
        self.width,self.height=10,10
        if(hovered): borderColour = (160,20,20)


        # Draw box
        if(noBorder): return(hovered)
        pygame.draw.circle(gui.screen, borderColour, (self.x,self.y), 10, 0)
        
        return(hovered)
