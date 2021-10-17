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

class dialogue():
    def __init__(self):
        self.initialised = False
        self.origText    = ''
        self.textArray   = []
        self.taP         = 1
        self.senPos      = 0
        self.timer       = 5
        self.colour      = (0,0,0)
        self.y           = 0
        self.y2          = 0

    def drawDialogue(self,gui,myfont, text,clicked, colour=(0, 128, 0), inBorder=True):
        sx,sy      = gui.bx + 100,gui.by+70
        x,y        = sx,sy
        maxWidth   = gui.bw - 200
        maxHeight  = sy + gui.bh - 200
        tRemaining = ""
        complete   = False

        # reset if called by new function
        if(self.origText!= text): 
            self.initialised=False
            self.origText = text

        if(self.initialised== False):
            # format paragraph into array of fitted sentences
            self.colour      = (0,0,0)
            self.origText    = text
            dAr,para = [], ""
            for word in text.split(' '):
                pre   = para
                para += word + " "
                textsurface = myfont.render(para, True, self.colour)
                w = textsurface.get_rect().width
                if(w>= maxWidth):
                    dAr.append(pre)
                    para = word + " "
            dAr.append(para)

            self.textArray = dAr
            self.initialised = True


        for sentence in range(0,len(self.textArray)):
            textsurface = myfont.render(self.textArray[sentence], True, self.colour)
            h = textsurface.get_rect().height
            gui.screen.blit(textsurface,(x,y))
            y = y + 2*h

            if(y + h >= maxHeight):
                tRemaining = self.textArray[sentence+1:]
                nextP = gui.nextButton.display(gui,noBorder=False)
                if(clicked and nextP): 
                    self.textArray = tRemaining
                break

        # fade in
        if(self.colour[0]<colour[0]):
            self.colour = ((self.colour[0]+2),(self.colour[1]+2),(self.colour[1]+2)   )
        else:
            complete=True


        return(complete)

    def drawScrollingDialogue(self,gui,myfont, text,clicked, colour=(0, 128, 0), inBorder=True,delay=1):
        sx,sy      = gui.bx + 100,gui.by+70
        x,y        = sx,sy
        maxWidth   = gui.bw - 200
        maxHeight  = sy + gui.bh - 200
        tRemaining = ""

        if(self.initialised== False):
            # format paragraph into array of fitted sentences
            self.y     = sy
            dAr,para = [], ""
            for word in text.split(' '):
                para += word + " "
                textsurface = myfont.render(para, True, colour)
                w = textsurface.get_rect().width
                if(w>= maxWidth):
                    dAr.append(para)
                    para = ""
            dAr.append(para)

            self.textArray = dAr
            self.initialised = True

        
        currentSentence = self.textArray[0]
        
        # Print fully preceeding row
        self.y2 = sy
        for row in range(0,self.taP-1):
            currentSentence = self.textArray[row]
            ts = myfont.render(currentSentence, True, colour)
            h = ts.get_rect().height
            gui.screen.blit(ts,(x,self.y2))
            self.y2=self.y2+2*h

        # scroll out this row
        for row in range(self.taP-1,self.taP):
            currentSentence = self.textArray[row]

            for word in (range(0,len(currentSentence[self.senPos]) )):
                printSentence = currentSentence[:self.senPos]
                ts = myfont.render(printSentence, True, colour)
                h = ts.get_rect().height
            gui.screen.blit(ts,(x,self.y))
            x=sx





        self.timer-=1
        if(self.timer<1):
            self.timer=delay
            if(len(currentSentence)-2 >=self.senPos):
                self.senPos+=1
            else:
                self.senPos=0
                self.taP +=1
                self.y=self.y+2*h


        """
        for sentence in range(0,len(self.textArray)):
            textsurface = myfont.render(self.textArray[sentence], True, self.colour)
            h = textsurface.get_rect().height
            gui.screen.blit(textsurface,(x,y))
            y = y + 2*h

            if(y + h >= maxHeight):
                tRemaining = self.textArray[sentence+1:]
                nextP = gui.nextButton.display(gui,noBorder=False)
                if(clicked and nextP): 
                    self.textArray = tRemaining
                break
        """







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

