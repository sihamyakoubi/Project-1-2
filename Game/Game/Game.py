import pygame

pygame.init()
pygame.display.set_caption ("Survivor") # titel van het programma (blauwe balk boven in)

size = width, height = 800, 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode(size) # scherm



time = pygame.time.Clock ()

def game_menu():
    menu = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        print (event)
    screen.fill(white)
    pygame.display.update()
    time.tick(60)

game_menu()