import pygame
import pygame.freetype


def render_button(screen, font, colour, x, y, text, sizex=150, sizey=50):
    pygame.draw.rect(screen, colour, ((x, y), (sizex, sizey)))
    font.render_to(screen, (x + 40, y + 18), text)


def on_click(event, x, y, sizex=150, sizey=50):
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("click")
            location = pygame.mouse.get_pos()
            if (location[0] > x) and (location[0] < x + sizex) and ((location[1] > y) and (location[1] < y + sizey)):
                return True
