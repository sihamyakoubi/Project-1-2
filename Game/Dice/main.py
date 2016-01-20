import sys, pygame
from random import randint #used in the dice() function, which generates a random number between 2 chosen integers.
pygame.init()

def dice():   # A function to return a random dice
    random = randint(1,6)  #generating a random number between 1 and 6
    if random == 1: # filtering the random number with if statements
        return pygame.image.load("img/1.png") #returning the pygame png printing function. 
    elif random == 2:
        return pygame.image.load("img/2.png")
    elif random == 3:
        return pygame.image.load("img/3.png")
    elif random == 4:
        return pygame.image.load("img/4.png")
    elif random == 5:
        return pygame.image.load("img/5.png")
    else:
        return pygame.image.load("img/6.png")

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
 
screen = pygame.display.set_mode(size)
 
dice = dice()  # het uitvoeren van de dice functie
dicerect = dice.get_rect() #vormt een rechthoek van de grootte van de het plaatje, in dit geval het plaatje van de dice

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        screen.fill(black)
        screen.blit(dice, dicerect) #met deze functie kun je - iets - in de window plaatsen, in dit geval de gebruikte functie dice. 
        pygame.display.flip()
