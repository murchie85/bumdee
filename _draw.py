from pygame.locals import *

def drawText(SCREEN,myfont, text,x,y, colour=(0, 128, 0),center='no',pos=None,limitWidth=None):
    hovered = None 
    textsurface = myfont.render(text, True, colour)
    
    # ========LIMIT TEXT LENGTH TO FIT
    if(limitWidth):
        if(textsurface.get_rect().width > limitWidth):
            maxLen = round(limitWidth/textsurface.get_rect().width * len(text))
            printText = text[0:maxLen-6] + '...'  
            textsurface = myfont.render(printText, True, colour)



    # Center info from infoBox
    if(center!='no'): x = x + (0.5*(int(center) - textsurface.get_rect().width))

    # If curser over text lightup
    if(pos!=None):
        textRect = Rect(x,y, x+textsurface.get_rect().width,y+textsurface.get_rect().height)
        if pos[0] > textRect.x and pos[0] < textRect.width:
            if pos[1] > textRect.y and pos[1] < textRect.height:
                textsurface = myfont.render(text, True, (128,0,0))
                hovered = text

    SCREEN.blit(textsurface,(x,y))
    return(hovered)


class imageAnimate():
    def __init__(self,p,f,s):
        self.p           = 0
        self.f           = 0
        self.s           = 0 
        self.initialised = False
        self.state       = None
    
    def animate(self,gui,gamestate,introSlides,pfs,blitPos):
        
        # ------Initialise

        if(self.state!=gamestate): self.initialised=False
        if(self.initialised==False):
            self.p           = pfs[0]
            self.f           = pfs[1]
            self.s           = pfs[2]
            self.state       = gamestate
            self.initialised =True

        # last frame
        end = len(introSlides)
        self.f -=1
        if(self.f<1):
            self.f=self.s
            self.p +=1 
            if(self.p>=end): self.p = 0

        gui.screen.blit(introSlides[self.p],blitPos)


def drawImage(screen,image,pos):
	screen.blit(image,pos)

def drawVerticleList(choices,selectedFont,x,y,gui,colour=(0, 0, 0) , spacing=2):
    
    yOffs  = 0
    hovered = None
    for c in choices:
        # Get Height
        sf = selectedFont.render(c, True, (0,0,0))
        height = sf.get_rect().height
        h = drawText(gui.screen,selectedFont,c,x,y+yOffs,colour,pos=(gui.mx,gui.my))
        if(h): hovered = h
        yOffs += spacing * height

    return(hovered)

