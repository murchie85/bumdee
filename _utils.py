import statistics
import pygame
import os

class stopTimer():
    def __init__(self):
        self.stopWatchInit  = False
        self.stopWatchState = None

    def stopWatch(self,countValue,source,trackedObject,gs):
        complete = False
        
        # Re-Initialise automatically
        if(self.stopWatchInit):
            if(self.stopWatchState['source']!= source or self.stopWatchState['endCount']!= countValue or self.stopWatchState['trackedObject']!= trackedObject):
                print('***initialising counter**** for : ' + str(source))
                self.stopWatchInit=False

        # Initialise stop watch 
        if(self.stopWatchInit==False):
            self.stopWatchState = {'elapsed': 0,'endCount':countValue,'source':source,'trackedObject':trackedObject}
            self.stopWatchInit=True

        if(self.stopWatchInit):
            self.stopWatchState['elapsed'] += gs.dt/1000
            #print('Iter: ' + str(self.itercount) + '  elapsed: ' + str(self.stopWatchState['elapsed']))
            if(self.stopWatchState['elapsed']>self.stopWatchState['endCount']):
                complete=True

        return(complete)

def stepGraph(label,valueList,graphHeight,startX, startY,hIncrement,font,gui,points=10,colour=(0,150,0)):
    """
    draws a graph
    ceiling is the max height from middle
    points...play with it
    """

    if(len(valueList)==0): return()


    textsurface = font.render(str(round(statistics.median(valueList),2)), True,  (230, 230, 255))
    gui.screen.blit(textsurface,(startX + 0.7*(points*hIncrement),startY+15))

    textColour = [(x+30 if x<255 else 255)for x in colour]
    textsurface = font.render(label, True, textColour)
    gui.screen.blit(textsurface,(startX + 0.1*(points*hIncrement),startY+15))



    maxVal    = max(valueList)
    minVal    = min(valueList)
    if(maxVal==0): maxVal =1
    squash    = (.5*graphHeight)/maxVal
    originY   = startY
    originX   = startX
    iterablePoints = points
    if(points>len(valueList)): iterablePoints = len(valueList)

    # Draw background box
    pygame.draw.rect(gui.screen,(0,0,0),[originX-5,originY-(0.5*graphHeight)-10,(points*hIncrement+5),graphHeight+10])



    # The line is at top if most values are closer to top wrt to ceiling, maybe can shift origin
    for x in range(0,iterablePoints):
        if(x==0):
            delta  = valueList[x] * squash
            endY   = startY 
            #endY   = startY - delta
        else:
            delta = (valueList[x] - valueList[x-1]) * squash
            endY = startY - delta

        if(x!=0):
            # vertical step
            pygame.draw.line(gui.screen,colour, [(startX),startY], [(startX),endY],2)
        startY = endY

        # step line
        # horizontal step
        pygame.draw.line(gui.screen,colour, [(startX),endY], [(startX+hIncrement),endY],1)
        startX = startX+hIncrement

    # Draw outline
    pygame.draw.rect(gui.screen,(0,200,0),[originX-5,originY-(0.5*graphHeight)-10,(points*hIncrement+5),graphHeight+10],3)


def importFiles(sName,tDir = 'pics/assets/mechBox/'):
    """
    for number of files bob1.jpg,bob2.jpg etc, sName=bob
    """
    tDir = tDir
    numLetters  = len(sName)
    numbers     = sorted([int("".join(filter(str.isdigit, x))) for x in os.listdir(tDir) if x[:numLetters] == sName])
    affix       = [x for x in os.listdir(tDir) if x[:numLetters] == sName][0].split('.')[-1]
    spriteList  = [sName + str(x) + '.' + affix for x in numbers]
    try:
        spriteList  = [pygame.image.load(tDir + x) for x in spriteList]
    except:
        print('Files can not be found for ' + str(sName))
        exit()
    return(spriteList)

def impFilesL(sName,tDir = 'pics/assets/mechBox/'):
    """
    Give the example of the first file i.e. bob1.jpg and it will import the rest
    """
    tDir = tDir
    affix       = '.' + str(sName.split('.')[-1])
    prefix      = str(sName.split('.')[0])[:-1]
    numLetters  = len(sName.split(affix)[0])
    numbers     = sorted([int("".join(filter(str.isdigit, x))) for x in os.listdir(tDir) if (prefix in x) and (affix in x)])
    spriteList  = [prefix + str(x) + affix for x in numbers]
    if(len(spriteList) < 1):
        print('spritelist not populated for ' + str(sName))
        exit()
    try:
        spriteList  = [pygame.image.load(tDir + x) for x in spriteList]
    except:
        print('Files can not be found for ' + str(sName))
        exit()
    return(spriteList)
