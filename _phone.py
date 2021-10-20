import pygame
from _draw import *
from datetime import datetime



class phone():
    def __init__(self,screenW,screenH, menuState='main'):

        self.screenW          = screenW
        self.screenH          = screenH
        self.menuState        = menuState
        self.screenOn         = 'off'
        self.navState         = None
        self.scrollerState    = 0
        self.msgDisplayIndex  = 0
        self.messageCache     = [1,'note','Something went wrong']
        self.musicCache       = [1,'solitude.mp3','music/solitude.mp3']

        self.mobilex       = 0
        self.mobiley       = 0.2*self.screenH
        self.mobileW       = 0.3*self.screenW
        self.mobileH       = 0.8*self.screenH

        #top widget
        self.mobiletx      = self.mobilex + 0.35*self.mobileW
        self.mobiletW      = 0.3*self.mobileW
        self.mobilety      = self.mobiley + 0.025*self.mobileH
        self.mobiletH      = 0.04*self.mobileH
        # screen
        self.mobileScreenx    = self.mobilex + 0.05*self.mobileW
        self.mobileSW         = 0.9*self.mobileW 
        self.mobileScreeny    = self.mobiley + 0.075*self.mobileH
        self.mobileSH         = 0.8*self.mobileH
        self.mobScreenBottom  = self.mobileScreeny + self.mobileSH 

        # sample charactrer
        self.sampleAvatar     = pygame.image.load('pics/characters/Chester.png')


        self.phoneStrip   = pygame.image.load('pics/phoneLogos/phoneStrip.png')
        self.bottomStrip  = pygame.image.load('pics/phoneLogos/bottomStrip.png')
        self.btmStrips    = [pygame.image.load('pics/phoneLogos/btmStrip1.png'),pygame.image.load('pics/phoneLogos/btmStrip2.png'),pygame.image.load('pics/phoneLogos/btmStrip3.png'),pygame.image.load('pics/phoneLogos/btmStrip4.png')]
        self.scrollStrips = [pygame.image.load('pics/phoneLogos/scrollStrip1.png'),pygame.image.load('pics/phoneLogos/scrollStrip2.png'),pygame.image.load('pics/phoneLogos/scrollStrip3.png'),pygame.image.load('pics/phoneLogos/scrollStrip4.png'),pygame.image.load('pics/phoneLogos/scrollStrip5.png'),pygame.image.load('pics/phoneLogos/scrollStrip6.png'),pygame.image.load('pics/phoneLogos/scrollStrip7.png'),pygame.image.load('pics/phoneLogos/scrollStrip8.png'),pygame.image.load('pics/phoneLogos/scrollStrip9.png'),pygame.image.load('pics/phoneLogos/scrollStrip10.png')]
        self.searchStrip  = pygame.image.load('pics/phoneLogos/searchStrip.png')

        self.musicStripOn  = [pygame.image.load('pics/music/musicOn1.png'),pygame.image.load('pics/music/musicOn2.png'),pygame.image.load('pics/music/musicOn3.png'),pygame.image.load('pics/music/musicOn4.png') ]
        self.musicStripOff = [pygame.image.load('pics/music/musicOff1.png'),pygame.image.load('pics/music/musicOff2.png'),pygame.image.load('pics/music/musicOff3.png'),pygame.image.load('pics/music/musicOff4.png') ]



        self.messageBox   = pygame.image.load('pics/sms/messageBox.png')

        self.messageLogo  = pygame.image.load('pics/phoneLogos/logos1.png')
        self.phoneLogo    = pygame.image.load('pics/phoneLogos/logos2.png')
        self.musicLogo    = pygame.image.load('pics/phoneLogos/logos3.png')
        self.clockLogo    = pygame.image.load('pics/phoneLogos/logos4.png')
        self.photoLogo    = pygame.image.load('pics/phoneLogos/logos5.png')
        self.mailLogo     = pygame.image.load('pics/phoneLogos/logos6.png')
        self.logos        = [(self.messageLogo,'message'),(self.phoneLogo,'phone'),(self.musicLogo,'music'),(self.clockLogo,'clock'),(self.photoLogo,'photo'),(self.mailLogo,'mail') ]





        self.greenA        = (39,65,45)
        self.greenB        = (82,128,58)
        self.greenC        = (173,195,63)
        self.greenD        = (215,233,149)
        self.screenDefault = (201,221,126)
        self.screenColour  = (201,221,126)

        self.greenBorder   = (127,187,73)
        self.darkGrey      = (44,52,56)
        self.lightGrey     = (72,77,79)


    # --------phone widgets/functions

    def mouseCollides(self,mousePos,x,y,w,h):
        if mousePos[0] > x and mousePos[0] < x + w:
            if mousePos[1] > y and mousePos[1] < y + h:
                return(True)
        return(False)

    def scroller(self,gui,parm=None):

        # ----- scroll up down using keys

        if(gui.userInput.returnedKey=='down'):
            if(self.scrollerState<9):
                self.scrollerState+=1
        if(gui.userInput.returnedKey=='up'):
            if(self.scrollerState>0):
                self.scrollerState-=1

        # -------Define scroller dimensions
        scrollerW,scrollerH = self.scrollStrips[self.scrollerState].get_rect().w,self.scrollStrips[0].get_rect().h
        scrollerX = self.mobileScreenx + self.mobileSW-1.5*scrollerW
        scrollerY = self.mobileScreeny + 0.15*self.mobileSH

        # ----- scroll up down using click

        if((gui.clicked) and (self.mouseCollides((gui.mx,gui.my),scrollerX,scrollerY,scrollerW,scrollerH)) ):
            if(gui.my < 0.7*(scrollerY+scrollerH)):
                if(self.scrollerState>0):
                    self.scrollerState-=1
            if(gui.my > 0.7*(scrollerY+scrollerH)):
                if(self.scrollerState<9):
                    self.scrollerState+=1

        # draw scroller frame
        drawImage(gui.screen,self.scrollStrips[self.scrollerState],(scrollerX,scrollerY))
        







    # --------MISC MENU

    def miscMenu(self,state,gui,gs):
        if(self.screenOn=='off'): return()

        drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
        self.navStrip(gui)



























    # ------------MESSAGES



    def displayMessage(self,gui,gs,message):
        if(self.screenOn=='off'): return()

        self.drawSelectedMessage(gui,message)
        self.navStrip(gui,previousState='message')
    
    def drawMessageBox(self,gui,messageSender,messageText,yset=None):

        selected = False
        trim=None
        # ---- set x y 

        x = self.mobileScreenx + 0.05 * self.mobileSW
        if(yset): 
            y = yset
        else:
            y = self.mobileScreeny + 0.11 * self.mobileSH

        # ----- set width height

        w,h = self.messageBox.get_rect().w ,self.messageBox.get_rect().h
        yOverflow = self.mobScreenBottom - (y+h)



        if((yOverflow<0) and y < self.mobScreenBottom): 
            trim=(0,0,w,h+yOverflow)

        # ----if message selected

        chosen = self.mouseCollides((gui.mx,gui.my),x,y,w,h)

        # -----Highlight chosen box

        if(chosen and trim==None): 
            pygame.draw.rect(gui.screen,self.greenC, (x, y,w , h),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
            if(gui.clicked):
                selected = True
        drawImage(gui.screen,self.messageBox,(x,y),trim=trim)
        
        stxt = drawText(gui.screen,gui.smallNokiaFont, messageSender,x+10,y+10, gui.greenA)
        gui.smsDialogue.drawDialogue(gui,gui.nanoFont, messageText,(x+10,y+10 + 1.2*stxt[2]),w-30,200,gui.clicked, gui.greenA)

        return(selected,(y+h))

    def drawSelectedMessage(self,gui,message,yset=None):

        messageSender = message[1]
        messageText   = message[2]
        if(len(message)==4):
            messageAvatar = pygame.image.load(message[3])
        else:
            messageAvatar = self.sampleAvatar

        selected = False
        trim=None
        # ---- set x y 

        x = self.mobileScreenx + 0.05 * self.mobileSW
        if(yset): 
            y = yset
        else:
            y = self.mobileScreeny + 0.05 * self.mobileSH

        # ----- set width height

        w,h = self.messageBox.get_rect().w ,self.messageBox.get_rect().h
        yOverflow = self.mobScreenBottom - (y+h)



        if((yOverflow<0) and y < self.mobScreenBottom): 
            trim=(0,0,w,h+yOverflow)

        # ----if message selected

        chosen = self.mouseCollides((gui.mx,gui.my),x,y,w,h)

        # -----Go to next apge

        if(chosen and trim and gui.clicked): 
            selected = True
        
        #----draw title

        stxt = drawText(gui.screen,gui.nokiaFont, messageSender,x+10,y+10, gui.greenA,center=0.85 * self.mobileSW)
        
        #----draw avatar
        imageW,imageH   = messageAvatar.get_rect().w,messageAvatar.get_rect().h
        halfWidth       = 0.5*(0.9*self.mobileSW - imageW)
        imageX,imageY   = x+halfWidth, y+10 + 1.2*stxt[2]
        
        
        pygame.draw.rect(gui.screen, self.greenC, (imageX, imageY,imageW , imageH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        thick=4
        pygame.draw.rect(gui.screen, self.greenA, (imageX-thick, imageY-thick,imageW+(2*thick) , imageH+(2*thick)),4,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        
        drawImage(gui.screen,messageAvatar,(imageX,imageY))
        #----draw text

        gui.smsDialogue.drawDialogue(gui,gui.smsFont, messageText,(x+20,imageY + 1.2* imageH),0.8*self.mobileSW,200,gui.clicked, gui.greenB,maxVerticleLines=5,verticalSep=1.3)

        return(selected,(y+h))





    def messageMenu(self,state,gui,gs):
        if(self.screenOn=='off'): return()
        #----------get message dimensions

        imgx,imgy = self.mobileScreenx + 40,self.mobileScreeny+0.14*self.mobileSH
        defaultY = imgy
        
        #----------- draw messages

        #todo improve
        self.msgDisplayIndex = self.scrollerState

        messageY=None
        for x in range(5):
            messageIndex = self.msgDisplayIndex + x

            #jump out at message limit
            if(messageIndex>=len(gs.messages)):
                break
            m = gs.messages[messageIndex]
            # Draw Message Boxes
            messageSender = m[1]
            messageText   = m[2]
            selected,nextY = self.drawMessageBox(gui,messageSender,messageText,yset=messageY)
            if(selected): 
                self.menuState    = 'displayMessage'
                self.messageCache = m
            messageY=nextY+10
 

        # ------draw top strip 
        
        drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
        
        # -----draw bottom nav 

        self.navStrip(gui)

        #------draw scroller right side 

        self.scroller(gui)
        






    def drawClock(self,state,gui,gs):
        if(self.screenOn=='off'): return()
        #----------get message dimensions



        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        x = self.mobileScreenx
        y = self.mobileScreeny + 0.35* self.mobileSH
        hovered,tw,th = drawText(gui.screen,gui.jumboFont, str(gs.date[-1]),x,y, gui.greenB,center=0.85 * self.mobileSW)
        y = y+1.2*th
        hovered,tw,th = drawText(gui.screen,gui.font, 'Real Time',x,y, gui.greenB,center=0.85 * self.mobileSW)
        y = y+1.2*th
        hovered,tw,th = drawText(gui.screen,gui.font, str(current_time),x,y, gui.greenB,center=0.85 * self.mobileSW)







        # ------draw top strip 
        
        drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
        
        # -----draw bottom nav 

        self.navStrip(gui)



    # ------------PHONE CONTACTS


    def phoneContactMenu(self,state,gui,gs):
        if(self.screenOn=='off'): return()
        #----------get message dimensions

        imgx,imgy = self.mobileScreenx + 40,self.mobileScreeny+0.14*self.mobileSH
        defaultY = imgy
        
        #----------- draw messages

        #todo improve
        self.msgDisplayIndex = self.scrollerState

        messageY=None
        for x in range(5):
            contactsIndex = self.msgDisplayIndex + x

            #jump out at message limit
            if(contactsIndex>=len(gs.contacts)):
                break
            m = gs.contacts[contactsIndex]
            # Draw Message Boxes
            contactP      = m[1]
            contactT      = m[2]
            selected,nextY = self.drawContactsBox(gui,contactP,contactT,yset=messageY,overflowy= (self.mobScreenBottom) )
            if(selected):
                print('Do something')
            messageY=nextY+10
 

        # ------draw top strip 
        
        drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
        
        # -----draw bottom nav 

        self.navStrip(gui)

        #------draw scroller right side 

        self.scroller(gui)
     

    def drawContactsBox(self,gui,contactP,contactT,yset=None,overflowy=None):

        selected = False
        trim=None
        # ---- set x y 

        x = self.mobileScreenx + 0.05 * self.mobileSW
        if(yset): 
            y = yset
        else:
            y = self.mobileScreeny + 0.11 * self.mobileSH

        # ----- set width height

        w,h = self.messageBox.get_rect().w ,0.8*self.messageBox.get_rect().h
        if(overflowy==None): overflowy = 0.8*self.mobScreenBottom
        yOverflow = overflowy - (y+h)



        if((yOverflow<0) and y < self.mobScreenBottom): 
            trim=(0,0,w,h+yOverflow)

        # ----if message selected

        chosen = self.mouseCollides((gui.mx,gui.my),x,y,w,h)

        # -----Highlight chosen box

        if(chosen and trim==None): 
            pygame.draw.rect(gui.screen,self.greenC, (x, y,w , h),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
            if(gui.clicked):
                selected = True
        
        pygame.draw.line(gui.screen, gui.greenB,(x,y),(0.7*self.mobileSW,y),3)
        

        hovered,tw,th = drawText(gui.screen,gui.nanoFont, contactT,x+10,y+20, gui.greenB)
        hovered,tw,th = drawText(gui.screen,gui.smallFont, contactP,x+10,y+20 + 1.2*th, gui.greenB)

        return(selected,(y+h))










































    # ------------MUSIC

    def musicMenu(self,state,gui,gs):
        if(self.screenOn=='off'): return()
        #----------get message dimensions

        imgx,imgy = self.mobileScreenx + 40,self.mobileScreeny+0.14*self.mobileSH
        defaultY = imgy
        
        #----------- draw messages

        #todo improve
        self.msgDisplayIndex = self.scrollerState

        messageY=None
        for x in range(5):
            musicIndex = self.msgDisplayIndex + x

            #jump out at message limit
            if(musicIndex>=len(gs.music)):
                break
            m = gs.music[musicIndex]
            # Draw Message Boxes
            musicTrack    = m[1]
            musicLoc      = m[2]
            selected,nextY = self.drawMusicBox(gui,musicTrack,musicLoc,yset=messageY,overflowy= (self.mobileScreeny + 0.73 * self.mobileSH) )
            if(selected): 
                self.menuState    = 'playMusic'
                self.musicCache   = m
            messageY=nextY+10
 
        # ------Draw control consol
        controlBoxY = self.mobileScreeny + 0.73 * self.mobileSH
        controlBoxW = 0.8*self.mobileSW
        controlBoxH = 0.2 * self.mobileSH
        controlBoxX = self.mobileScreenx + (0.5*(0.9*self.mobileSW - controlBoxW))
        pygame.draw.rect(gui.screen, (180,204,90),    (controlBoxX, controlBoxY,controlBoxW , controlBoxH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, (48,98,48),    (controlBoxX, controlBoxY,controlBoxW , controlBoxH),7,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        

        # ----- draw music buttons 

        controlCenterX = 0.8*(controlBoxX + (controlBoxW/2))
        controlCenterY = (controlBoxY + (controlBoxH/4))

        imgw,imgh = self.musicStripOff[0].get_rect().w,self.musicStripOff[0].get_rect().h
        
        # ---- draw current track
        gui.smsDialogue.drawDialogue(gui,gui.nanoFont, self.musicCache[1],(controlBoxX+20,controlCenterY+(1.1*imgh) ),0.9*controlBoxW,200,gui.clicked, gui.greenB,maxVerticleLines=1)

        #------- manage music buttons

        rwnd = drawSelectableImage(self.musicStripOff[1],self.musicStripOn[1],(controlCenterX - (1.5*imgw),controlCenterY),gui,trim=False)
        if(rwnd):
            trackno = self.musicCache[0] - 1
            if(trackno>0):
                self.musicCache   =  gs.music[trackno]

        play = drawSelectableImage(self.musicStripOff[2],self.musicStripOn[2],(controlCenterX,controlCenterY),gui,trim=False)
        if(play):
            self.menuState    = 'playMusic'
        ffwd = drawSelectableImage(self.musicStripOff[0],self.musicStripOn[0],(controlCenterX + (1.5*imgw),controlCenterY),gui,trim=False)
        if(ffwd):
            trackno = self.musicCache[0] + 1
            if(trackno<len(gs.music)):
                self.musicCache   =  gs.music[trackno]


        # ------draw top strip 
        
        drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
        
        # -----draw bottom nav 

        self.navStrip(gui)

        #------draw scroller right side 

        self.scroller(gui)
        

    
    def drawMusicBox(self,gui,track,trackLoc,yset=None,overflowy=None):

        selected = False
        trim=None
        # ---- set x y 

        x = self.mobileScreenx + 0.05 * self.mobileSW
        if(yset): 
            y = yset
        else:
            y = self.mobileScreeny + 0.11 * self.mobileSH

        # ----- set width height

        w,h = self.messageBox.get_rect().w ,0.8*self.messageBox.get_rect().h
        if(overflowy==None): overflowy = 0.8*self.mobScreenBottom
        yOverflow = overflowy - (y+h)



        if((yOverflow<0) and y < self.mobScreenBottom): 
            trim=(0,0,w,h+yOverflow)

        # ----if message selected

        chosen = self.mouseCollides((gui.mx,gui.my),x,y,w,h)

        # -----Highlight chosen box

        if(chosen and trim==None): 
            pygame.draw.rect(gui.screen,self.greenC, (x, y,w , h),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
            if(gui.clicked):
                selected = True
        
        pygame.draw.line(gui.screen, gui.greenB,(x,y),(0.7*self.mobileSW,y),3)
        
        gui.smsDialogue.drawDialogue(gui,gui.musicFont, track,(x+10,y+20),w-30,200,gui.clicked, gui.greenB)

        return(selected,(y+h))

    def playMusic(self,state,gui,gs,musicArray):
        tune = musicArray[2]
        gui.music.play(tune)
        self.menuState = 'music'








    # ------------PHONE

    def drawPhone(self,state,gui,gs):

        # -------Update navs

        if(self.navState == 'home'): self.menuState = 'main'
        if(self.navState == 'message'): self.menuState = 'message'

        self.navState = None

        # ------phone screen On/Off 
        
        self.screenOn = state
        pos = (gui.mx,gui.my)
        collides = self.mouseCollides(pos,self.mobileScreenx,self.mobileScreeny,self.mobileSW,self.mobileSH)
        if(collides): self.screenOn='on'
        if(collides==False): self.screenOn='off'
        if(self.screenOn=='on'): self.screenColour = self.screenDefault
        if(self.screenOn=='off'): self.screenColour = (78,96,9)

        # ----------Draw physical phone
        # phone
        pygame.draw.rect(gui.screen, self.darkGrey,    (self.mobilex, self.mobiley,self.mobileW , self.mobileH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, self.greenBorder, (self.mobilex, self.mobiley,self.mobileW , self.mobileH),7,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # top widget
        pygame.draw.rect(gui.screen, self.darkGrey,   (self.mobiletx, self.mobilety,self.mobiletW , self.mobiletH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, self.greenBorder,    (self.mobiletx, self.mobilety,self.mobiletW , self.mobiletH),4,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)


        #screen 
        pygame.draw.rect(gui.screen, self.screenColour, (self.mobileScreenx, self.mobileScreeny,self.mobileSW , self.mobileSH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, self.greenBorder,  (self.mobileScreenx, self.mobileScreeny,self.mobileSW , self.mobileSH),7,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # circle button
        pygame.draw.circle(gui.screen, self.lightGrey, (self.mobilex + 0.48*self.mobileW, self.mobileScreeny + self.mobileSH + 35), 25, 0)
        pygame.draw.circle(gui.screen, self.greenBorder, (self.mobilex + 0.48*self.mobileW, self.mobileScreeny + self.mobileSH + 35), 25, 3)



        # ----------Navigate states

        if(self.menuState == 'message'): 
            self.messageMenu(state,gui,gs)
        elif(self.menuState== 'displayMessage'):
            self.displayMessage(gui,gs,self.messageCache)
        elif(self.menuState== 'music'):
            self.musicMenu(state,gui,gs)
        elif(self.menuState== 'phone'):
            self.phoneContactMenu(state,gui,gs)
        elif(self.menuState=='playMusic'):
            self.playMusic(state,gui,gs,self.musicCache)
        elif(self.menuState=='clock'):
            self.drawClock(state,gui,gs)
        else:
            self.miscMenu(state,gui,gs)

        



        # ---------home screen 
        if(self.screenOn=='on' and self.menuState == 'main'):

            imgx,imgy = self.mobileScreenx + 40,self.mobileScreeny+0.14*self.mobileSH
            defaultY = imgy
            
            # draw strips 
            drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
            drawImage(gui.screen,self.searchStrip,(self.mobileScreenx,self.mobileScreeny + 0.7*self.mobileSH))
            self.navStrip(gui)


            for i in range(0,len(self.logos)):
                img  = self.logos[i][0]
                txt  = self.logos[i][1]
                imgw = img.get_rect().w
                imgh = img.get_rect().h


                pCollides = self.mouseCollides(pos,imgx,imgy,imgw,imgh)
                if(pCollides):
                    pygame.draw.rect(gui.screen,self.greenC, (imgx, imgy,imgw , imgh),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
                    drawImage(gui.screen,img,(imgx,imgy))
                    if(gui.clicked):
                        self.menuState = txt
                        print(str(txt) + 'Logo Clicked')
                        
                else:
                    drawImage(gui.screen,img,(imgx,imgy))
                imgx+=100
                if(i>1):
                    imgy = defaultY + 130
                if(i==2):
                    imgx = self.mobileScreenx + 40









    #---------------NAVIGATION

    def navStrip(self,gui,previousState='home'):
        # Get coordinates
        navY,navH =self.mobileScreeny+self.mobileSH-41,self.btmStrips[0].get_rect().h
        imageWidth = self.btmStrips[0].get_rect().w

        leftArrowX,leftArrowW  = (self.mobileScreenx + 0.16*imageWidth),0.07*imageWidth
        circleX,circleW = (self.mobileScreenx + 0.42*imageWidth),0.07*imageWidth
        squareX,squareW = (self.mobileScreenx + 0.655*imageWidth),0.07*imageWidth

        if(self.mouseCollides((gui.mx,gui.my),leftArrowX,navY,leftArrowW,navH ) ):
            drawImage(gui.screen,self.btmStrips[1],(self.mobileScreenx,self.mobileScreeny+self.mobileSH-41))
            if(gui.clicked):
                self.navState = previousState
                return()
                
        elif(self.mouseCollides((gui.mx,gui.my),circleX,navY,circleW,navH ) ):
            drawImage(gui.screen,self.btmStrips[2],(self.mobileScreenx,self.mobileScreeny+self.mobileSH-41))
            if(gui.clicked): 
                self.navState = 'home'
                return()
        elif(self.mouseCollides((gui.mx,gui.my),squareX,navY,squareW,navH ) ):
            drawImage(gui.screen,self.btmStrips[3],(self.mobileScreenx,self.mobileScreeny+self.mobileSH-41))

        else:
            drawImage(gui.screen,self.btmStrips[0],(self.mobileScreenx,self.mobileScreeny+self.mobileSH-41))






#---------------DIALOGUE CLASS





class smsDialogue():
    def __init__(self):
        self.initialised = False
        self.origText    = ''
        self.textArray   = []
        self.taP         = 0
        self.senPos      = 0
        self.colour      = (0,0,0)
        self.y           = 0
        self.y2          = 0

    def drawDialogue(self,gui,myfont, text,pos,maxWidth,maxHeight,clicked, colour=(0, 0, 0),skip=False,verticalSep=1.1,maxVerticleLines=2,displayNextButton=False):
        sx,sy = pos[0],pos[1]
        x,y        = sx,sy
        tRemaining = ""
        complete   = False
        hovered    = gui.mouseCollides((gui.mx,gui.my),x,y,maxWidth,maxHeight)



        # reset if called by new function
        if(self.origText!= text): 
            self.initialised=False
            self.origText = text

        if(self.initialised== False):
            # format paragraph into array of fitted sentences
            self.origText    = text
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

        hTotal = 0
        for sentence in range(0,len(self.textArray)):
            textsurface = myfont.render(self.textArray[sentence], True, colour)
            h = textsurface.get_rect().height
            gui.screen.blit(textsurface,(x,y))
            y = y + verticalSep*h
            hTotal = hTotal + verticalSep*h


            # if display capped 
            if((sentence>=maxVerticleLines-1)): break
            # If height capped
            if(hTotal >= maxHeight):
                tRemaining = self.textArray[sentence+1:]
                if(displayNextButton): nextP = gui.nextButton.display(gui,noBorder=False)
                
                if(clicked and hovered and (len(tRemaining)>0)):
                    self.textArray = tRemaining
                break

            complete  = True
            


        return(complete)


            