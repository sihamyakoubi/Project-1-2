import pygame

pygame.init()
width, height = 800, 600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
screen = pygame.display.set_mode((width,height))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill (white)
    pygame.display.update()
    