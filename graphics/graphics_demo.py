# Imports
import pygame
import math

# Initialize game engine
pygame.init()


# Window
WIDTH = 800
HEIGHT = 600
TITLE = "My Awesome Picture"
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption(TITLE)


# Timer
clock = pygame.time.Clock()
refresh_rate = 60


# Colors
DPINK = (240, 105, 102)
GREEN = (106, 190, 131)
BLUE = (49, 155, 187)
WHITE = (255, 255, 255)
BLACK = (50, 51, 56)
LPINK = (241, 172 , 157)
    

# Game loop
done = False

while not done:
    # Event processing (React to key presses, mouse clicks, etc.)
    ''' for now, we'll just check to see if the X is clicked '''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True


    # Game logic (Check for collisions, update points, etc.)
    ''' leave this section alone for now ''' 

    # Drawing code (Describe the picture. It isn't actually drawn yet.)
    screen.fill(WHITE)
    pygame.draw.rect(screen, DPINK, [50, 50, 400, 300])
    pygame.draw.line(screen, GREEN, [300, 40], [100,500], 5)
    pygame.draw.ellipse(screen, LPINK, [100, 100, 600, 300])
    pygame.draw.polygon(screen, BLACK, [[200, 200], [50,400], [600, 500]], 10)

    ''' angles for arcs are measured in radians (a pre-cal topic) '''
    pygame.draw.arc(screen, LPINK, [100, 100, 100, 100], 0, math.pi/2, 1)
    pygame.draw.arc(screen, BLACK, [100, 100, 100, 100], 0, math.pi/2, 50)


    # Update screen (Actually draw the picture in the window.)
    pygame.display.flip()


    # Limit refresh rate of game loop 
    clock.tick(refresh_rate)


# Close window and quit
pygame.quit()
