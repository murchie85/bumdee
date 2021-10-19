import pygame
from _draw import *
class phone():
    def __init__(self,screenW,screenH, menuState='main'):

        self.screenW       = screenW
        self.screenH       = screenH
        self.menuState     = menuState
        self.screenOn      = 'off'

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


        self.phoneStrip   = pygame.image.load('pics/phoneLogos/phoneStrip.png')
        self.bottomStrip  = pygame.image.load('pics/phoneLogos/bottomStrip.png')
        self.searchStrip  = pygame.image.load('pics/phoneLogos/searchStrip.png')

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


    def mouseCollides(self,mousePos,x,y,w,h):
        if mousePos[0] > x and mousePos[0] < x + w:
            if mousePos[1] > y and mousePos[1] < y + h:
                return(True)
        return(False)


    def drawMessageBox(self,gui,messageSender,messageText,yset=None):

        x = self.mobileScreenx + 0.05 * self.mobileSW
        y = self.mobileScreeny + 0.11 * self.mobileSH
        if(yset): y = yset
        w,h = self.messageBox.get_rect().w ,self.messageBox.get_rect().h

        chosen = self.mouseCollides((gui.mx,gui.my),x,y,w,h)

        # Highlight chosen box
        if(chosen):
            pygame.draw.rect(gui.screen,self.greenC, (x, y,w , h),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        drawImage(gui.screen,self.messageBox,(x,y))
        stxt = drawText(gui.screen,gui.smallNokiaFont, messageSender,x+10,y+10, gui.greenA)
        gui.smsDialogue.drawDialogue(gui,gui.nanoFont, messageText,(x+10,y+10 + 1.2*stxt[2]),w-30,200,gui.clicked, gui.greenB)

        return(y+h)

    def messageMenu(self,state,gui):
        if(self.screenOn=='off'): return()

        imgx,imgy = self.mobileScreenx + 40,self.mobileScreeny+0.14*self.mobileSH
        defaultY = imgy
        
        # draw strips 
        drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
        drawImage(gui.screen,self.bottomStrip,(self.mobileScreenx,self.mobileScreeny+self.mobileSH-41))
        
        # Draw Message Boxes
        messageSender = 'Clive'
        messageText   = "Yo, I missed you last week. How have you been?"
        nextY = self.drawMessageBox(gui,messageSender,messageText)
        nextY = self.drawMessageBox(gui,messageSender,messageText,yset=nextY+10)
        nextY = self.drawMessageBox(gui,messageSender,messageText,yset=nextY+10)
        nextY = self.drawMessageBox(gui,messageSender,messageText,yset=nextY+10)



    def drawPhone(self,state,gui):
        
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
        pygame.draw.rect(gui.screen, self.darkGrey,   (self.mobiletx, self.mobilety,self.mobiletW , self.mobiletH),border_radius=1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
        pygame.draw.rect(gui.screen, self.greenBorder,    (self.mobiletx, self.mobilety,self.mobiletW , self.mobiletH),4,border_radius=1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)


        #screen 
        pygame.draw.rect(gui.screen, self.screenColour, (self.mobileScreenx, self.mobileScreeny,self.mobileSW , self.mobileSH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(gui.screen, self.greenBorder,  (self.mobileScreenx, self.mobileScreeny,self.mobileSW , self.mobileSH),7,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # circle button
        pygame.draw.circle(gui.screen, self.lightGrey, (self.mobilex + 0.48*self.mobileW, self.mobileScreeny + self.mobileSH + 35), 25, 0)
        pygame.draw.circle(gui.screen, self.greenBorder, (self.mobilex + 0.48*self.mobileW, self.mobileScreeny + self.mobileSH + 35), 25, 3)



        # ----------Navigate states

        if(self.menuState == 'message'): self.messageMenu(state,gui)
        



        # ---------home screen 
        if(self.screenOn=='on' and self.menuState == 'main'):

            imgx,imgy = self.mobileScreenx + 40,self.mobileScreeny+0.14*self.mobileSH
            defaultY = imgy
            
            # draw strips 
            drawImage(gui.screen,self.phoneStrip,(self.mobileScreenx,self.mobileScreeny))
            drawImage(gui.screen,self.searchStrip,(self.mobileScreenx,self.mobileScreeny + 0.7*self.mobileSH))
            drawImage(gui.screen,self.bottomStrip,(self.mobileScreenx,self.mobileScreeny+self.mobileSH-41))
            


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

    def drawDialogue(self,gui,myfont, text,pos,maxWidth,maxHeight,clicked, colour=(0, 128, 0),skip=False,verticalSep=1.1,maxVerticleLines=2,displayNextButton=False):
        sx,sy = pos[0],pos[1]
        x,y        = sx,sy
        self.colour = colour
        tRemaining = ""
        complete   = False
        hovered    = gui.mouseCollides((gui.mx,gui.my),x,y,maxWidth,maxHeight)



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

        hTotal = 0
        for sentence in range(0,len(self.textArray)):
            textsurface = myfont.render(self.textArray[sentence], True, self.colour)
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


            