import pygame
# zeker niet gejat
def main():
    """ Set up the game and run the main game loop """
    pygame.init()      # Prepare the pygame module for use
    surface_sz = 700   # Desired physical surface size, in pixels.

    # Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((surface_sz, surface_sz))

    # Set up some data to describe a small rectangle and its color
    small_rect = (300, 200, 150, 90)
    some_color = (255, 255, 255)        # A color is a mix of (Red, Green, Blue)

    while True:
        ev = pygame.event.poll()    # Look for any event
        if ev.type == pygame.QUIT:  # Window close button clicked?
            break                   #   ... leave game loop

        # Update your game objects and data structures here...

        # We draw everything from scratch on each frame.
        # So first fill everything with the background color
        main_surface.fill((250, 255, 255))

        my_font = pygame.font.SysFont("Courier", 100)
        the_text = my_font.render("Menu", True, (0,0,0))
        main_surface.blit(the_text, (225, 10))
        # Overpaint a smaller rectangle on the main surface
        # main_surface.fill(some_color, small_rect)

        # Now the surface is ready, tell pygame to display it!
        pygame.display.flip()

    pygame.quit()     # Once we leave the loop, close the window.

main()
print ("hello world" )
print ("het werkt - Minde ")
print ("het werkt -  lennard")
print ("het werkt - Sam is veranderd")
print ("het werkt - Siham")