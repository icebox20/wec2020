import pygame
import pygame.freetype


def render_box(screen, colour, x, y):
    pygame.draw.rect(screen, colour, ((x, y), (50, 50)))
