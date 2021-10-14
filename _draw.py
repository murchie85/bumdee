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