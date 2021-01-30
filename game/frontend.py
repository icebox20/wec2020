import pygame
import pygame.freetype
import ChessEngine

pygame.init()
pygame.font.init()
font = pygame.freetype.SysFont("SansitaOne.tff",25)
size = 10
screenx = (size*50)+80 + 200
screeny = (size*50)+80
screen = pygame.display.set_mode([screenx, screeny])

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (142, 142, 142)
SILVER = (192, 192, 192)
LIGHT = (252, 204, 116)
DARK = (87, 58, 46)
GREEN = (0, 255, 0)
RED = (215, 0, 0)
ORANGE = (255, 165, 0)

#           0     1     2    3     4     5     6      7    8     9     10    11    12    13
pieces = ['wP', 'wB', 'wR', 'wN', 'wQ', 'wK', 'wV', 'bP', 'bB', 'bR', 'bN', 'bQ', 'bK', 'bV']
IMAGES = {}


def load_images():
    for piece in pieces:
        # print("assets/chess_pieces/" + piece + ".png")
        IMAGES[piece] = pygame.transform.scale(pygame.image.load("assets/chess_pieces/" + piece + ".png"), (50, 50))


def coords_to_notation(coords):
    return int(((coords[1] - 50) /(50))), int(((coords[0] - 50) /(50)))


def notation_to_coords(notation):
    convert = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7, "h": 8, "i": 9, "j": 10, "k": 11, "l": 12}
    if isinstance(notation, str):
        return 40 + 50 * (convert[notation] - 1)

    return 40 + 50 * (size - notation)


def draw_squares(screen, size=8):
    colour_dict = {True: LIGHT, False: DARK}
    current_colour = True
    for row in range(size):
        for square in range(size):
            pygame.draw.rect(screen, colour_dict[current_colour], ((40 + (square * 50)), 40 + (row * 50), 50, 50))
            current_colour = not current_colour
        current_colour = not current_colour


def draw_coords(screen, font, size):
    for row in range(size):
        font.render_to(screen, (10, 45 + (row * 50)), str(size - row))
    for col in range(size):
        font.render_to(screen, (45 + (col * 50), (size + 1) * 50), chr(65 + col))


def draw_piece(screen, piece, x, y):
    for row in range(size):
        font.render_to(screen, (10, 45 + (row * 50)), str(size - row))
    for col in range(size):
        font.render_to(screen, (45 + (col * 50), (size + 1) * 50), chr(65 + col))


def display_board(screen):
    test = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["--", "--", "--", "--", "--", "--", "--", "--"],
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        ["wR", "wN", "wB", "wK", "wQ", "wB", "wN", "wR"]
    ]

    for i, row in enumerate(game.board[sizeToBoard[size]]):
        for j, piece in enumerate(row):
            if piece == "--":
                pass
            else:
                screen.blit(IMAGES[piece], pygame.Rect(notation_to_coords(size - (j)), notation_to_coords(size - (i)), 50, 50))


def move_piece(start, end):
    print("Move", start, end)
    move = ChessEngine.Move(start,end,game.board[sizeToBoard[size]] )
    game.makeMove(move, sizeToBoard[size] )

running = True
load_images()
firstClick = ()
secondClick = ()

sizeToBoard = {8: 0, 10: 1, 12: 2, 14:3, 16:4}

game = ChessEngine.GameState()

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            location = pygame.mouse.get_pos()
            print("Location:", location)
            if(location[0] > ((size * 50) + 40)) or (location[1] > ((size * 50) + 40)):
                pass
            elif firstClick == ():
                firstClick = location
                print("Frist:", coords_to_notation(firstClick))
            else:
                secondClick = location
                print("Second:", coords_to_notation(secondClick))
                move_piece(coords_to_notation(firstClick), coords_to_notation(secondClick))
                #print(game.board[0])
                firstClick = ()
            if ((location[0] > (screenx - 40 - 150)) and (location[0] < (screenx - 40))) and ((location[1] > screeny/2) and (location[1] < (screeny/2)+50)):
                print("Undo")
                game.undoMove(sizeToBoard[size])



    screen.fill((255, 255, 255))

    draw_squares(screen, size)
    pygame.draw.rect(screen, ORANGE,((screenx - 40 - 150,screeny/2),(150,50)))
    font.render_to(screen, (screenx - 40 - 150 + 40,(screeny/2) + 20) , "Undo")
    draw_coords(screen, font, size)
    display_board(screen)
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
