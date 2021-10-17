from _draw       import *
from _effects    import *




def askQuestion(text,gs,gui,fx,user_input,returnValue,fade=False,setCounterTime=1):

    # Initialise
    if(gs.counter==None): 
        gs.counter = setCounterTime
        user_input.returnedKey=''

    valueToUpdate = None
    # Set Fade wait
    if(fade): 
        fi = fx.fadeIn(gui)
        if(user_input.returnedKey=='return' and fi!=True):
            fi = fx.fadeIn(gui,skip=True)
            user_input.returnedKey=''
    else:
        fi = True

    if(fi):
        text = text.upper()
        
        r = gui.dialogue.drawDialogue(gui,gui.font, text,gui.clicked, colour=(180, 180, 180))
        if(r):
            user_input.processInput()
            user_input.drawTextInput(user_input.enteredString,0.42*gui.width,0.35*gui.height)
            if(user_input.returnedKey=='complete'):
                valueToUpdate  = user_input.enteredString
                gs.tempState   = returnValue 
                gs.counter -=1
                if(gs.counter<1): 
                    gs.counter=None
                    return(valueToUpdate)
        elif(user_input.returnedKey=='return'):
            # skip 
            user_input.returnedKey=''
            r = gui.dialogue.drawDialogue(gui,gui.font, text,gui.clicked, colour=(180, 180, 180),skip=True)



    return(valueToUpdate)


def questionResponse(text,gs,gui,user_input,returnValue,setCounterTime=20,setInputVal=False):

    # Set Counter if uninitialised
    if(gs.counter==None): gs.counter = setCounterTime
    
    skip = False
    if(user_input.returnedKey=='return'):
        skip=True
        user_input.returnedKey=''


    nc = gui.dialogue.drawDialogue(gui,gui.font, text,gui.clicked, colour=(180, 180, 180),pos=(0.33*gui.width,0.35*gui.height),skip=skip)
    if(nc):
        gs.counter -=1
        if(gs.counter<1):
            gs.counter = gs.initCounter
            gs.tempState=returnValue
            if(setInputVal!=False):
                user_input.enteredString = setInputVal
                gs.counter = None



def scrollingResponse(titleText,diaText, gs,gui,user_input,setCounterTime=20,titlePos=(300,300),sPos=None,delay=5):
    # init sPos
    if(sPos==None): sPos = (titlePos[0]+200,titlePos[1]+100)

    # Set Counter if uninitialised
    if(gs.counter==None): gs.counter = setCounterTime
    
    # skip title
    titleSkip,skip = False, False
    if(user_input.returnedKey=='return' and gs.functionState==None):
        titleSkip=True
        user_input.returnedKey=''


    # --------Draw Title Dialogue
    titleLoad = gui.dialogue.drawDialogue(gui,gui.font,titleText,gui.clicked, colour=(180, 180, 180),pos=titlePos,fade=False,skip=titleSkip)
    
    if(titleLoad and gs.functionState==None):
        gs.counter -=1
        if(gs.counter<1):
            gs.counter = None
            gs.functionState = 'scrollingText'
    

    # ------ Draw scrolling text
    # Skip if needed(dodgy and needs fixing)
    if(user_input.returnedKey=='return' and gs.functionState=='scrollingText'):
        skip=True

    if(gs.functionState == 'scrollingText'):
        st = gui.sDialogue.drawScrollingDialogue(gui,gui.font, diaText,gui.clicked, colour=(0, 128, 0),pos=sPos,delay=delay,skip=skip)
        if(st):
            gs.functionState = 'finalise'

    if(gs.functionState=='finalise'):
        gui.sDialogue.drawScrollingDialogue(gui,gui.font, diaText,gui.clicked, colour=(0, 128, 0),pos=sPos,delay=delay,skip=skip)
        if(user_input.returnedKey=='return'):
            user_input.returnedKey = ""   
            gui.sDialogue.initialised = False
            gs.functionState = None
            gs.counter=None
            return(True)




    return(False)


