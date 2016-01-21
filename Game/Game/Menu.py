import pygame
pygame.init()
pygame.display.set_caption ("Survivor") # titel van het programma (blauwe balk boven in)

width, height = 700, 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode((width,height)) # scherm
time = pygame.time.Clock ()


def quitGame():
    pygame.quit()
    quit()

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def button(msg,x,y,w,h,ic,ac,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    print(click)
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(screen, ac,(x,y,w,h))

        if click[0] == 1 and action != None:
            action()         
    else:
        pygame.draw.rect(screen, ic,(x,y,w,h))

    smallText = pygame.font.SysFont("comicsansms",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( (x+(w/2)), (y+(h/2)) )
    screen.blit(textSurf, textRect)

def game_menu():
    menu = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitGame()
        print (event)
        screen.fill(white)
        largeText = pygame.font.SysFont("comicsansms",115)
        TextSurf, TextRect = text_objects("Survivor", largeText)
        TextRect.center = ((width*0.5),(height*0.15))
        screen.blit(TextSurf, TextRect)

        
        button("Start",width*0.45,height*0.4,100,50,white,black,None)
        button("Load Game",width*0.45,height*0.5,100,50,white,black,None)
        button("Setting",width*0.45,height*0.6,100,50,white,black,None)
        button("Quit",width*0.45,height*0.7,100,50,white,black,quitGame)
        button("Help",width*0.9,height*0.9,50,50,white,black,Help_Menu)

        
        pygame.display.update()
        time.tick(60)

def Help_Menu():
    while True:
        Help = pygame.image.load("content/Help.png")
        Help = pygame.transform.scale(Help,(width,height))
        screen.blit(Help, (0,0 ))
        button("X",width-20,0,20,20,red,white,game_menu)
             
        pygame.display.update()
        time.tick(60)
        pygame.display.set_mode((width,height))  

game_menu()