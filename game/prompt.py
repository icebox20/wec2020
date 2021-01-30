from button import render_button, on_click


def ask_for_size(screen, font, pygame):
    screen = pygame.display.set_mode([300, 450])

    pygame.display.set_caption("WEC2021 Chess")
    pygame.display.set_icon(pygame.transform.scale(pygame.image.load("assets/chess_pieces/wP.png"), (32, 32)))

    size = 16
    done = True
    while done:
        screen.fill((255, 255, 255))
        font.render_to(screen, (50,50), "Select Board Size")
        for i in range(5):
            render_button(screen, font, (255, 165, 0), 80 , 100 + (i*60),  str(8+(i*2)))
            #print(100 + (i*60))
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            if on_click(event, 80, 100):
                return True, 8
            if on_click(event, 80, 160):
                return True, 10
            if on_click(event, 80, 220):
                return True, 12
            if on_click(event, 80, 280):
                return True, 14
            if on_click(event, 80, 340):
                return True, 16
    return False, size
