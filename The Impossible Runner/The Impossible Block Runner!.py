import pygame
from pygame.locals import *
pygame.init()
pygame.mixer.init()
wSurface = pygame.display.set_mode((1000,700))
pygame.display.set_caption("The Impossible Block Runner!")
lvl = pygame.image.load("pygame project level 1.png")
losing = pygame.mixer.Sound('losing.ogg')
start = False
pickcolor = False
bc = (0,0,0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
stop = 250
clock = pygame.time.Clock()
basicFont = pygame.font.SysFont(None, 100)
rc = 0
while 1:
    clock.tick(300)
    if start == False: #Controls menu
        wSurface.fill((0,204,204))
        titletext = basicFont.render("The Impossible Runner!", True, WHITE, (0,204,204))
        titletextRect = titletext.get_rect()
        titletextRect.centerx = wSurface.get_rect().centerx
        titletextRect.top = 1
        wSurface.blit(titletext, titletextRect)
        controlstext = basicFont.render("Controls:", True, WHITE, (0,204,204))
        controlstextRect = titletext.get_rect()
        controlstextRect.left = 0
        controlstextRect.top = 200
        wSurface.blit(controlstext, controlstextRect)
        uparrowtext = basicFont.render("Use the up arrow key to jump.", True, WHITE, (0,204,204))
        uparrowtextRect = titletext.get_rect()
        uparrowtextRect.left = 0
        uparrowtextRect.top = 300
        wSurface.blit(uparrowtext, uparrowtextRect)
        continuetext = basicFont.render("Press any key to continue!", True, WHITE, (0,204,204))
        continuetextRect = titletext.get_rect()
        continuetextRect.left = 70
        continuetextRect.top = 500
        wSurface.blit(continuetext, continuetextRect)
        for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.quit()
                if ev.type == KEYDOWN:
                    start = True
        pygame.display.update()
    else: 
        if pickcolor == False: #Color selection menu
            wSurface.fill((0,204,204))
            picktext = basicFont.render("Pick a color for your runner!", True, WHITE, ((0,204,204)))
            picktextRect = titletext.get_rect()
            picktextRect.left = 50
            picktextRect.top = 1
            wSurface.blit(picktext, picktextRect)
            blrect = pygame.draw.rect(wSurface,BLACK,(183,100,150,150))
            wrect = pygame.draw.rect(wSurface,WHITE,(633,100,150,150))
            rrect = pygame.draw.rect(wSurface,RED,(183,300,150,150))
            brect = pygame.draw.rect(wSurface,BLUE,(633,300,150,150))
            grect = pygame.draw.rect(wSurface,GREEN,(400,500,150,150))
            if pygame.mouse.get_pressed()[0] == 1:
                if blrect.collidepoint(pygame.mouse.get_pos()) or wrect.collidepoint(pygame.mouse.get_pos()) or rrect.collidepoint(pygame.mouse.get_pos()) or brect.collidepoint(pygame.mouse.get_pos()) or grect.collidepoint(pygame.mouse.get_pos()): #Check if they've selected a color
                    if blrect.collidepoint(pygame.mouse.get_pos()):
                        bc = BLACK
                    elif wrect.collidepoint(pygame.mouse.get_pos()):
                        bc = WHITE
                    elif rrect.collidepoint(pygame.mouse.get_pos()):
                        bc = RED
                    elif brect.collidepoint(pygame.mouse.get_pos()):
                        bc = BLUE
                    elif grect.collidepoint(pygame.mouse.get_pos()):
                        bc = GREEN
                    pickcolor = True
            for ev in pygame.event.get():
                if ev.type == QUIT:
                    pygame.quit()
            pygame.display.update()
        else:
            if stop < 0: #If the player had reached the end
                text = basicFont.render("You Win!", True, BLACK, WHITE)
                textRect = text.get_rect()
                textRect.centerx = wSurface.get_rect().centerx
                textRect.centery = wSurface.get_rect().centery
                wSurface.blit(text, textRect)
                for ev in pygame.event.get():
                    if ev.type == QUIT:
                        pygame.quit()
                stop-=1
                pygame.display.update()
            if stop == -300: #Close the program after it shows the winning screen
                wSurface.fill((255,255,255))
                pygame.quit()
                pygame.display.update()
            if stop == 250: #If you've died and are restarting
                pygame.mixer.music.load('BG MUSIC.ogg')
                pygame.mixer.music.play(-1) #Plat music again
                jump = 0
                y = 547
                c = 0
                counter = 0
                j = 0
                stop = 0
                wSurface.fill((0,0,0))
                clock = pygame.time.Clock()
                pygame.draw.rect(wSurface,BLUE,(0,500,1200,200))
                blockrect = pygame.draw.rect(wSurface,GREEN,(150,y,25,25))
                spikes = []
                saferect = []
                rects = []
                #Append all rects
                spikes.append(pygame.Rect((480,525),(35,50)))
                spikes.append(pygame.Rect((610,525),(35,50)))
                rects.append(pygame.Rect((776,522),(50,50)))
                rects.append(pygame.Rect((849,484),(50,90)))
                rects.append(pygame.Rect((923,444),(50,130)))
                spikes.append(pygame.Rect((930,350),(35,50)))
                rects.append(pygame.Rect((1092,522),(273,50)))
                rects.append(pygame.Rect((1090,360),(300,98)))
                spikes.append(pygame.Rect((1468,525),(35,50)))
                spikes.append(pygame.Rect((1588,525),(35,50)))
                spikes.append(pygame.Rect((1715,525),(35,50)))
                spikes.append(pygame.Rect((1822,455),(35,50)))
                rects.append(pygame.Rect((1905,522),(50,50)))
                rects.append(pygame.Rect((1978,484),(50,90)))
                spikes.append(pygame.Rect((2081,455),(35,50)))
                rects.append(pygame.Rect((2163,522),(50,50)))
                spikes.append(pygame.Rect((2171,428),(35,50)))
                rects.append(pygame.Rect((2236,484),(50,90)))
                spikes.append(pygame.Rect((2171,280),(35,50)))
                spikes.append(pygame.Rect((2295,380),(35,50)))
                spikes.append(pygame.Rect((2081,455),(35,50)))
                rects.append(pygame.Rect((2165,378),(50,45)))
                rects.append(pygame.Rect((2286,330),(50,45)))
                rects.append(pygame.Rect((2072,410),(50,45)))
                spikes.append(pygame.Rect((2554,525),(35,50)))
                spikes.append(pygame.Rect((2618,455),(35,50)))
                rects.append(pygame.Rect((2703,522),(50,50)))
                rects.append(pygame.Rect((2775,484),(50,90)))
                spikes.append(pygame.Rect((2782,383),(35,50)))
                rects.append(pygame.Rect((2922,522),(273,50)))
                spikes.append(pygame.Rect((2984,475),(35,50)))
                spikes.append(pygame.Rect((3098,475),(35,50)))
                rects.append(pygame.Rect((3214,472),(50,50)))
                rects.append(pygame.Rect((3276,436),(50,50)))
                rects.append(pygame.Rect((3342,410),(50,50)))
                spikes.append(pygame.Rect((3350,310),(35,50)))
                rects.append(pygame.Rect((3414,458),(273,50)))
                spikes.append(pygame.Rect((3486,408),(35,50)))
                spikes.append(pygame.Rect((3608,408),(35,50)))
                spikes.append(pygame.Rect((3829,525),(35,50)))
                spikes.append(pygame.Rect((3970,525),(35,50)))
                spikes.append(pygame.Rect((4106,525),(35,50)))
                rects.append(pygame.Rect((4207,472),(273,50)))
                spikes.append(pygame.Rect((4565,525),(35,50)))
                spikes.append(pygame.Rect((4691,525),(35,50)))
                spikes.append(pygame.Rect((4811,525),(35,50)))
                rects.append(pygame.Rect((4950,525),(273,50)))
                rects.append(pygame.Rect((5007,497),(273,50)))
                rects.append(pygame.Rect((5087,448),(273,50)))
                spikes.append(pygame.Rect((5164,400),(35,50)))
                spikes.append(pygame.Rect((5261,400),(35,50)))
                spikes.append(pygame.Rect((5457,525),(35,50)))
                spikes.append(pygame.Rect((5581,525),(35,50)))
                spikes.append(pygame.Rect((5702,525),(35,50)))
                saferect.append(pygame.Rect((776,471),(50,1)))
                saferect.append(pygame.Rect((849,393),(50,1)))
                saferect.append(pygame.Rect((923,313),(50,1)))
                saferect.append(pygame.Rect((1092,471),(273,1)))
                saferect.append(pygame.Rect((1090,261),(300,1)))
                saferect.append(pygame.Rect((1905,471),(50,1)))
                saferect.append(pygame.Rect((1978,393),(50,1)))
                saferect.append(pygame.Rect((2163,471),(50,1)))
                saferect.append(pygame.Rect((2236,393),(50,1)))
                saferect.append(pygame.Rect((2165,332),(50,1)))
                saferect.append(pygame.Rect((2286,284),(50,1)))
                saferect.append(pygame.Rect((2072,364),(50,1)))
                saferect.append(pygame.Rect((2703,471),(50,1)))
                saferect.append(pygame.Rect((2775,393),(50,1)))
                saferect.append(pygame.Rect((2922,471),(273,1)))
                saferect.append(pygame.Rect((3214,421),(50,1)))
                saferect.append(pygame.Rect((3276,385),(50,1)))
                saferect.append(pygame.Rect((3342,359),(50,1)))
                saferect.append(pygame.Rect((3414,407),(273,1)))
                saferect.append(pygame.Rect((4207,421),(273,1)))
                saferect.append(pygame.Rect((4950,474),(273,1)))
                saferect.append(pygame.Rect((5007,446),(273,1)))
                saferect.append(pygame.Rect((5087,397),(273,1)))
                #Make adjustments to rects
                for x in range(len(saferect)):
                    saferect[x].top+=rects[x].height-2
                    saferect[x].height = 10
                saferect.append(pygame.Rect((0,570),(6000,10)))
                for x in range(len(spikes)):
                    if x == 2 or x == 6 or x == 7 or x == 8 or x == 9 or x == 10 or x == 13 or x == 14 or x == 17:
                        spikes[x].height = 30
                        spikes[x].top-=10
                    else:
                        spikes[x].height = 30
                        spikes[x].top+=20
                    spikes[x].width = 25
                    spikes[x].left+=5
            if stop > 0: #If they've hit a something and lost
                text = basicFont.render("You Lose!", True, WHITE, BLACK)
                textRect = text.get_rect()
                textRect.centerx = wSurface.get_rect().centerx
                textRect.centery = wSurface.get_rect().centery
                wSurface.blit(text, textRect)
                for ev in pygame.event.get():
                    if ev.type == QUIT:
                        pygame.quit()
                stop+=1
                pygame.display.update()
            counter += 2 #Add to counter for level and rect movement
            if stop == 0: #If nothing has happened and the game should continue normally
                pygame.display.set_caption("The Impossible Block Runner! | Attempts: {}".format(rc)) #Update the caption
                j = 0
                for ev in pygame.event.get():
                    if ev.type == QUIT:
                        pygame.quit()
                    if ev.type == KEYDOWN:
                        if ev.key == K_UP:
                            for x in saferect:
                                if blockrect.colliderect(x): #If they're on top of a block or on the ground allow the jump
                                    jump = 1
                if jump == 1:
                    if c == 22:
                        jump = 0
                        c = 0
                    else:
                        c+=1
                        y-=4
                elif jump == 0:
                    for x in saferect:
                        if blockrect.colliderect(x): #Check if they're on a block or the ground
                            j = 1
                    if j == 0: #If not on a block gravity pulls them on
                        y+=4
                wSurface.blit(lvl,(0-counter,0)) #Blit the entire level, taking account for movement with counter
                #Move all of the rects
                for x in rects:
                    x = pygame.Rect((x.left-counter, x.top),(x.width,x.height))
                    #pygame.draw.rect(wSurface, (0,255,0), x) #Used for debugging
                for x in spikes:
                    x = pygame.Rect((x.left-counter, x.top),(x.width,x.height))
                    #pygame.draw.rect(wSurface, (0,255,0), x) #Used for debugging
                for x in saferect:
                    x = pygame.Rect((x.left-counter, x.top),(x.width,x.height))
                    #pygame.draw.rect(wSurface, (0,0,255), x) # Used for debugging
                #Check for collision with rects
                for x in spikes:
                    if blockrect.colliderect(x) == 1:
                        stop += 1 #Add to stop for the if statement in the loop
                        rc+=1 #Add to attempts counter
                        losing.play()
                        pygame.mixer.music.stop() #Stop music
                for x in rects:
                   if blockrect.colliderect(x) == 1:
                        stop += 1 #Add to stop for the if statement in the loop
                        rc+=1 #Add to attempts counter
                        losing.play() 
                        pygame.mixer.music.stop() #Stop music
                #Check if the player has won
                if blockrect.colliderect(pygame.Rect((5950,0),(50,700))):
                    stop = -1 #Make stop -1 for if statement
                    pygame.mixer.music.stop() #Stop music                       
                #Move block, and draw the block
                pygame.draw.rect(wSurface,bc,(150,y,25,25))
                blockrect = pygame.Rect((150+counter,y,25,25))
                pygame.display.update()
