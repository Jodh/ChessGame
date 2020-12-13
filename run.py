import sys, pygame

from ChessBoard import ChessBoard

pygame.init()

size = 300, 300
screen = pygame.display.set_mode(size)
board = ChessBoard(screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            board.handleMouseClick(pygame.Vector2(pygame.mouse.get_pos()))

    board.handleMousePos(pygame.Vector2(pygame.mouse.get_pos()))
    board.draw()
    pygame.display.flip()
