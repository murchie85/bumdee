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


def iterateImages(screen,introSlides,p,f,s,blitPos):
    end = len(introSlides)
    
    f -=1
    if(f<1):
        f=s
        p +=1 
        if(p>=end): p = 0

    screen.blit(introSlides[p],blitPos)

    return(p,f)

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

