# Simple pygame program

# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (142, 142, 142)
SILVER = (192, 192, 192)
LIGHT = (252, 204, 116)
DARK = (87, 58, 46)
GREEN = (0, 255, 0)
RED = (215, 0, 0)
ORANGE = (255, 165, 0)

def draw_squares(screen):
    colour_dict = {True: LIGHT, False: DARK}
    current_colour = True
    for row in range(8):
        for square in range(8):
            pygame.draw.rect(screen, colour_dict[current_colour], ((40 + (square * 50)), 40 + (row * 50), 50, 50))
            current_colour = not current_colour
        current_colour = not current_colour

# Run until the user asks to quit
running = True
while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with white
    screen.fill((255, 255, 255))

    # Draw a solid blue circle in the center
    draw_squares(screen)

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()