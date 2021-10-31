from pygame.locals import *
import pygame

def drawText(SCREEN,myfont, text,x,y, colour=(0, 128, 0),center='no',pos=None,limitWidth=None):
    """ Center means giving the far x point """
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


def drawTextandBox(SCREEN,myfont, x,y,label, value, textColour=(215, 233, 149),boxColour=(15,56,15),lineColour=(139,172,15),pos=None,minBoxWidth=3):
    """ 
        Text + box i.e. myvalue [009] 
        
        for more functionality make new function
    """
    hovered = None 
    labelsurface        = myfont.render(label, True, textColour)
    tw = labelsurface.get_rect().width
    th = labelsurface.get_rect().height


    # TextBox Values
    smallestSurface = myfont.render('S', True, textColour)
    x2           = x + tw + smallestSurface.get_rect().height
    y2           = y
    if(len(value)<minBoxWidth): value = str(''.join(['0' for x in range(minBoxWidth-len(value))]) )  +str(value)
    valuesurface = myfont.render(value, True, textColour)
    tw2          = valuesurface.get_rect().width
    th2          = valuesurface.get_rect().height

    bw = tw2 + 1.5*smallestSurface.get_rect().width
    bh = th2 + smallestSurface.get_rect().height
    bx = x2 - 0.75*smallestSurface.get_rect().width
    by = y2 - 0.5*smallestSurface.get_rect().height


    # If curser over label lightup
    if(pos!=None):
        labelRect = Rect(x,y, x+labelsurface.get_rect().width,y+labelsurface.get_rect().height)
        if pos[0] > labelRect.x and pos[0] < labelRect.width:
            if pos[1] > labelRect.y and pos[1] < labelRect.height:
                labelsurface = myfont.render(label, True, (128,0,0))
                hovered = label

    SCREEN.blit(labelsurface,(x,y))

    # draw box and shading
    pygame.draw.rect(SCREEN, (boxColour), [bx, by,bw ,bh])
    pygame.draw.line(SCREEN,(lineColour), (bx,by+bh),(bx+bw,by+bh),3)
    pygame.draw.line(SCREEN,(lineColour), (bx+bw,by),(bx+bw,by+bh),3)
    
    SCREEN.blit(valuesurface,(x2,y2))

    txe2 = bx + bw
    the2 = by + bh
    return(txe2,the2)


def drawTextandBoxGrid(SCREEN,myfont, x,y,pairArray, textColour=(215, 233, 149),boxColour=(15,56,15),lineColour=(139,172,15),pos=None,minBoxWidth=3):
    """ 
        Text + box i.e. myvalue [009] 
        
        for more functionality make new function
    """
    widthArray = []
    rhsArray   = []
    for i in pairArray: widthArray.append(myfont.render(i[0], True, textColour).get_rect().width)
    tw = max(widthArray)

    for j in pairArray:
        label, value = j[0],j[1]
        hovered = None 
        labelsurface        = myfont.render(label, True, textColour)
        th = labelsurface.get_rect().height


        # TextBox Values
        smallestSurface = myfont.render('S', True, textColour)
        x2           = x + tw + 2*smallestSurface.get_rect().height
        y2           = y
        if(len(value)<minBoxWidth): value = str(''.join(['0' for x in range(minBoxWidth-len(value))]) )  +str(value)
        valuesurface = myfont.render(value, True, textColour)
        tw2          = valuesurface.get_rect().width
        th2          = valuesurface.get_rect().height

        bw = tw2 + 1.5*smallestSurface.get_rect().width
        bh = th2 + smallestSurface.get_rect().height
        bx = x2 - 0.75*smallestSurface.get_rect().width
        by = y2 - 0.5*smallestSurface.get_rect().height


        bw2 = tw + 1.5*smallestSurface.get_rect().width
        bh2 = th + smallestSurface.get_rect().height
        bx2 = x - 0.75*smallestSurface.get_rect().width
        by2 = y - 0.5*smallestSurface.get_rect().height



        # If curser over label lightup
        if(pos!=None):
            labelRect = Rect(x,y, x+labelsurface.get_rect().width,y+labelsurface.get_rect().height)
            if pos[0] > labelRect.x and pos[0] < labelRect.width:
                if pos[1] > labelRect.y and pos[1] < labelRect.height:
                    labelsurface = myfont.render(label, True, (128,0,0))
                    hovered = label




        # draw box and shading
        pygame.draw.rect(SCREEN, (boxColour), [bx2, by2,bw2 ,bh2])
        pygame.draw.line(SCREEN,(lineColour), (bx2,by2+bh2),(bx2+bw2,by2+bh2),4)
        pygame.draw.line(SCREEN,(lineColour), (bx2+bw2,by2),(bx2+bw2,by2+bh2),4)

        SCREEN.blit(labelsurface,(x,y))

        # draw box and shading
        pygame.draw.rect(SCREEN, (boxColour), [bx, by,bw ,bh])
        pygame.draw.line(SCREEN,(lineColour), (bx,by+bh),(bx+bw,by+bh),4)
        pygame.draw.line(SCREEN,(lineColour), (bx+bw,by),(bx+bw,by+bh),4)
        
        SCREEN.blit(valuesurface,(x2,y2))

        y = y +bh + (0.3*bh)

        #append the right side, so it can be 
        # worked out what is longest
        rhsArray.append((bx + bw))


    # return xend,yend
    txe2 = max(rhsArray)
    the2 = by + bh

    return(txe2,the2)











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
    def __init__(self,p,f,s,name=None):
        self.p           = 0
        self.f           = 0
        self.s           = 0 
        self.initialised = False
        self.state       = None
        self.name        = None
    
    def animate(self,gui,gamestate,introSlides,pfs,blitPos):
        """p = page f = count s = reset count
        """
        
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

def drawTxtBtn(image,image2,pos,gui,text,font=None,txtColour=(215,233,149),yadj=0.3):
    
    # ------draw image

    displayImage = image
    hover = gui.mouseCollides((gui.mx,gui.my),pos[0],pos[1],image.get_rect().w,image.get_rect().h)
    if(hover): displayImage = image2
    gui.screen.blit(displayImage,pos)


    #-------draw text
    if(font==None): font = gui.smallFont
    textsurface = font.render(text, True, txtColour)
    tw = textsurface.get_rect().width
    th = textsurface.get_rect().height
    x  = pos[0]+(0.5*(image.get_rect().w - tw))
    y  = pos[1]+(yadj*(image.get_rect().h - th))
    gui.screen.blit(textsurface,(x,y))



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

