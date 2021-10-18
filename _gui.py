import pygame
from _draw import *

class gui():
    def __init__(self,white, screen, width, height,font,bigFont,smallFont,themeColour,exitButton,nextButton,dialogue,sDialogue,music,clicked=False):
        self.white         = white
        self.screen        = screen
        self.width         = width
        self.height        = height
        self.font          = font
        self.bigFont       = bigFont
        self.smallFont     = smallFont
        self.themeColour   = themeColour
        self.exitButton    = exitButton
        self.nextButton    = nextButton
        self.dialogue      = dialogue
        self.sDialogue     = sDialogue
        self.music         = music
        self.clicked       = clicked

        self.greenA        = (39,65,45)
        self.greenB        = (82,128,58)
        self.greenC        = (173,195,63)
        self.greenD        = (215,233,149)
        self.screenDefault = (201,221,126)
        self.screenColour  = (201,221,126)

        self.greenBorder   = (127,187,73)
        self.darkGrey      = (44,52,56)
        self.lightGrey     = (72,77,79)


        self.mobilex       = 0
        self.mobiley       = 0.22*self.height
        self.mobileW       = 0.27*self.width
        self.mobileH       = 0.78*self.height

        #top widget
        self.mobiletx      = self.mobilex + 0.35*self.mobileW
        self.mobiletW      = 0.3*self.mobileW
        self.mobilety      = self.mobiley + 0.025*self.mobileH
        self.mobiletH      = 0.04*self.mobileH
        # screen
        self.mobileSx      = self.mobilex + 0.05*self.mobileW
        self.mobileSW      = 0.9*self.mobileW
        self.mobileSy      = self.mobiley + 0.075*self.mobileH
        self.mobileSH      = 0.8*self.mobileH

        self.messageLogo  = pygame.image.load('pics/phoneLogos/logos1.png')
        self.phoneLogo    = pygame.image.load('pics/phoneLogos/logos2.png')
        self.musicLogo    = pygame.image.load('pics/phoneLogos/logos3.png')
        self.clockLogo    = pygame.image.load('pics/phoneLogos/logos4.png')
        self.photoLogo    = pygame.image.load('pics/phoneLogos/logos5.png')
        self.mailLogo     = pygame.image.load('pics/phoneLogos/logos6.png')
        self.logos        = [(self.messageLogo,'message'),(self.phoneLogo,'phone'),(self.musicLogo,'music'),(self.clockLogo,'clock'),(self.photoLogo,'photo'),(self.mailLogo,'mail') ]


        self.mx     = 0
        self.my     = 0


        self.menuBG = None

    def border(self,colour=(128,0,0)):
        self.bx,self.by = 0.1*self.width,0.1*self.height
        self.bw,self.bh = 0.8*self.width,0.8*self.height
        rect = pygame.draw.rect(self.screen, colour, [self.bx, self.by,self.bw , self.bh],4)


    def semiBorder(self):
        # Bottom Line
        pygame.draw.line(self.screen,self.greenBorder,(0,self.height-5),(self.width ,self.height-5),7)
        
        # right Line
        pygame.draw.line(self.screen,self.greenBorder,(self.width-4,0.08*self.height),(self.width-4,self.height),9)
        
        # top horizontal Line
        pygame.draw.line(self.screen,self.greenBorder,(0.7*self.width , 0.08*self.height),((self.width),0.08*self.height),7)

        # top vert Line
        pygame.draw.line(self.screen,self.greenBorder,(0.7*self.width+3 , 0.08*self.height),(0.7*self.width+3,0),7)

        # fill in black box
        pygame.draw.rect(self.screen, (0,0,0),    (0.7*self.width+3, 0,0.3*self.width , 0.08*self.height))




    def drawPhone(self,state):
        self.screen.fill((39,65,45))
        

        # ------phone screen 

        pos = (self.mx,self.my)
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.mobileSx and pos[0] < self.mobileSx + self.mobileSW:
            if pos[1] > self.mobileSy and pos[1] < self.mobileSy + self.mobileSH:
                state='on'
        if(state=='on'): self.screenColour = self.screenDefault
        if(state=='off'): self.screenColour = (78,96,9)




        # phone
        pygame.draw.rect(self.screen, self.darkGrey,    (self.mobilex, self.mobiley,self.mobileW , self.mobileH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(self.screen, self.greenBorder, (self.mobilex, self.mobiley,self.mobileW , self.mobileH),7,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # top widget
        pygame.draw.rect(self.screen, self.darkGrey,   (self.mobiletx, self.mobilety,self.mobiletW , self.mobiletH),border_radius=1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)
        pygame.draw.rect(self.screen, self.greenBorder,    (self.mobiletx, self.mobilety,self.mobiletW , self.mobiletH),4,border_radius=1, border_top_left_radius=-1, border_top_right_radius=-1, border_bottom_left_radius=-1, border_bottom_right_radius=-1)


        #screen 
        pygame.draw.rect(self.screen, self.screenColour, (self.mobileSx, self.mobileSy,self.mobileSW , self.mobileSH),border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)
        pygame.draw.rect(self.screen, self.greenBorder,  (self.mobileSx, self.mobileSy,self.mobileSW , self.mobileSH),7,border_radius=4, border_top_left_radius=4, border_top_right_radius=4, border_bottom_left_radius=4, border_bottom_right_radius=4)

        # circle button
        pygame.draw.circle(self.screen, self.lightGrey, (self.mobilex + 0.48*self.mobileW, self.mobileSy + self.mobileSH + 35), 25, 0)
        pygame.draw.circle(self.screen, self.greenBorder, (self.mobilex + 0.48*self.mobileW, self.mobileSy + self.mobileSH + 35), 25, 3)



        imgx,imgy = self.mobileSx + 40,self.mobileSy+50
        for i in range(0,len(self.logos)):
            img = self.logos[i][0]
            txt = self.logos[i][1]

            drawImage(self.screen,img,(imgx,imgy))
            imgx+=100
            if(i>1):
                imgy = self.mobileSy+200
            if(i==3):
                imgx = self.mobileSx + 10
        
