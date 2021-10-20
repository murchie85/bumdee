from pygame.locals import *

def drawText(SCREEN,myfont, text,x,y, colour=(0, 128, 0),center='no',pos=None,limitWidth=None):
    hovered = None 
    textsurface = myfont.render(text, True, colour)
    tw = textsurface.get_rect().width
    th = textsurface.get_rect().height
    
    # ========LIMIT TEXT LENGTH TO FIT
    if(limitWidth):
        if(textsurface.get_rect().width > limitWidth):
            maxLen = round(limitWidth/textsurface.get_rect().width * len(text))
            printText = text[0:maxLen-6] + '...'  
            textsurface = myfont.render(printText, True, colour)
            tw = textsurface.get_rect().width
            th = textsurface.get_rect().height



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
    return(hovered,tw,th)


def approachColour(baseColour,targetColour,inc=2):
    complete = False
    if(baseColour[0]<targetColour[0]):
        baseColour = ((baseColour[0]+inc),(baseColour[1]),(baseColour[2]))
    if(baseColour[1]<targetColour[1]):
        baseColour = ((baseColour[0]),(baseColour[1]+inc),(baseColour[2]))
    if(baseColour[2]<targetColour[2]):
        baseColour = ((baseColour[0]),(baseColour[1]),(baseColour[2]+inc))

    if(baseColour==targetColour): complete=True

    return(complete,baseColour)

class dialogue():
    def __init__(self):
        self.initialised = False
        self.origText    = ''
        self.textArray   = []
        self.taP         = 0
        self.senPos      = 0
        self.colour      = (0,0,0)
        self.y           = 0
        self.y2          = 0

    def drawDialogue(self,gui,myfont, text,maxWidth,maxHeight,clicked, colour=(0, 128, 0), inBorder=True,pos=(-1,-1),fade=True,skip=False):
        #(0, 128, 126)
        if(pos==(-1,-1)):
            sx,sy      = gui.bx + 100,gui.by+70
        else:
            sx,sy = pos[0],pos[1]
        
        x,y        = sx,sy
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
        if(fade):
            complete,self.colour = approachColour(self.colour,colour,inc=2)
            if(skip):
                complete  = True
                self.colour = colour
        else:
            complete  = True
            self.colour = colour

        return(complete)


class scrollingDialogue():
    def __init__(self):
        self.initialised = False
        self.origText    = ''
        self.textArray   = []
        self.taP         = 0
        self.senPos      = 0
        self.timer       = 5
        self.colour      = (0,0,0)
        self.y           = 0
        self.y2          = 0

    def drawScrollingDialogue(self,gui,myfont, text,clicked, colour=(0, 128, 0), inBorder=True,delay=0,pos=(-1,-1),skip=False):
        if(pos==(-1,-1)):
            sx,sy      = gui.bx + 100,gui.by+70
        else:
            sx,sy = pos[0],pos[1]
        x,y        = sx,sy
        maxWidth   = gui.bw - 200
        maxHeight  = sy + gui.bh - 200
        tRemaining = ""
        self.finished = False

        if(self.initialised== False):
            print('initialising for ')
            print(text)
            # format paragraph into array of fitted sentences
            self.textArray  = []
            self.y          = sy
            self.senPos     =0
            self.taP        =0

            dAr,para = [], ""
            for word in text.split(' '):
                pre   = para
                para += word + " "
                textsurface = myfont.render(para, True, colour)
                w = textsurface.get_rect().width
                if(w>= maxWidth):
                    dAr.append(pre)
                    para = word + " "
            dAr.append(para)

            self.textArray = dAr
            self.initialised = True


        # Print fully preceeding row
        self.y2 = sy
        for row in range(0,self.taP):
            currentSentence = self.textArray[row]
            ts = myfont.render(currentSentence, True, colour)
            h = ts.get_rect().height
            gui.screen.blit(ts,(x,self.y2))
            self.y2=self.y2+2*h


        # scroll out this row
        currentSentence = self.textArray[self.taP]
        for word in (range(0,len(currentSentence[self.senPos]) )):
            printSentence = currentSentence[:self.senPos]
            ts = myfont.render(printSentence, True, colour)
            h = ts.get_rect().height
        gui.screen.blit(ts,(x,self.y))
        x=sx


        # Skip if needbe
        if(skip and self.taP<(len(self.textArray)-1)): 
            self.taP = len(self.textArray)-1
            self.senPos=0
            self.y=self.y+2*(len(self.textArray)-1)*h

        self.timer-=1
        if(self.timer<1):
            self.timer=delay
            if(len(currentSentence)-2 >=self.senPos):
                self.senPos+=1
            else:
                if(len(self.textArray)-2>=self.taP):
                    self.taP +=1
                    self.y=self.y+2*h
                    self.senPos=0
                else:
                    self.finished    = True

        return(self.finished)




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


def drawImage(screen,image,pos,trim=False):
    if(trim!=False):
        screen.blit(image,pos,trim)
    else:
        screen.blit(image,pos)

def drawSelectableImage(image,image2,pos,gui,trim=False):
    displayImage = image

    hover = gui.mouseCollides((gui.mx,gui.my),pos[0],pos[1],image.get_rect().w,image.get_rect().h)
    if(hover): displayImage = image2

    if(trim!=False):
        gui.screen.blit(displayImage,pos,trim)
    else:
        gui.screen.blit(displayImage,pos)

    if(hover and gui.clicked):
        return(True)

    return(False)



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

