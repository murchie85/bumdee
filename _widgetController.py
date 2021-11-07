from _draw import *

def showWidgNode(gui,x,y,headerText="Widget",bodyText="Widget textX",selectable=True,flashAlert=False):
    selected = False
    
    
    selected = drawSelectableImage(gui.widgetNode[0],gui.widgetNode[1],(x,y),gui,trim=False)
    
    if(flashAlert):
        gui.widgetAnim.animate(gui,'showWidgNode',[gui.widgetNode[0],gui.widgetNode[2]],(0,10,10),(x,y))

    w = gui.widgetNode[0].get_rect().w

    

    hovered,tw,th= drawText(gui.screen,gui.nanoNokiaFont, headerText, x,y+8, gui.greenD,center=w)
    drawText(gui.screen,gui.nanoNokiaFont, bodyText, x,y+37, gui.greenD,center=w)
    
    if(selectable==False): return(False)
    
    return(selected)



def manageWidget(x,y,gui,phone,gs,fx,desktop,widgetFunction,headerText,bodyText,adargs=None):


    selected   = False 
    selectable = True

    
    #-------------only one widget at a time
    # ------------If a widget is active disable all others
    if(gs.ACTIVEWIDGET!=None): selectable = False 
    
    selected = showWidgNode(gui,x,y,headerText=headerText,bodyText=bodyText,selectable=selectable)

    if(adargs=='demoWidgetAlert'):
        showWidgNode(gui,x,y,headerText=headerText,bodyText=bodyText,selectable=False,flashAlert=True)
        return()


    if(selected): gs.ACTIVEWIDGET = widgetFunction



def widgetCoordinator(gui,phone,gs,fx,desktop,commands,commandArg=None):
    """
    widgets are drawn to board first, then logic so pop up window comes after
    """

    if('recycle' in commands[0]):
    	manageWidget(gs.junk.x,gs.junk.y,gui,phone,gs,fx,desktop,'recycleCenter',"Pull Tab","Tabs Collected: " + str(gs.totalCantabs),adargs=commandArg)
    
    if('forex' in commands[0]):
    	manageWidget(gs.forex.x,gs.forex.y,gui,phone,gs,fx,desktop,'forexExchange',"Forex Exchange","Profit £" +str(gs.returnProfit),adargs=commandArg)


    if('recycle' in commands[0]): gs.junk.recycleCenter(gui,gs,fx,desktop,phone)
    
    if('forex' in commands[0]): gs.forex.forexExchange(gui,gs,fx,desktop,phone)
    