from typing import Optional, List

from Pieces.Bishop import Bishop
from Pieces.Horse import Horse
from Pieces.King import King
from Pieces.Queen import Queen
from Pieces.Rook import Rook

import pygame

from Pieces.ChessPiece import ChessPiece
from Pieces.Pawn import Pawn
from Utils.Colours import Colour


class ChessBoard(object):
    def __init__(self, screen: pygame.Surface, size: int = 8):
        self.screen = screen
        self.size = size
        self._hovered = None
        self._clicked = None
        self.moves = None
        self._board: List[List[Optional[ChessPiece]]] = [[None for _ in range(size)] for _ in range(size)]
        self.reset()

    def reset(self):
        row = lambda colour, row: [
            Rook(self.screen, colour, (0, row), self._board),
            Horse(self.screen, colour, (1, row), self._board),
            Bishop(self.screen, colour, (2, row), self._board),
            King(self.screen, colour, (3, row), self._board),
            Queen(self.screen, colour, (4, row), self._board),
            Bishop(self.screen, colour, (5, row), self._board),
            Horse(self.screen, colour, (6, row), self._board),
            Rook(self.screen, colour, (7, row), self._board)
        ]

        self._board[0] = row(Colour.white, 0)

        self._board[1] = [Pawn(self.screen, Colour.white, (i, 1), self._board) for i in range(self.size)]

        self._board[len(self._board) - 2] = [Pawn(self.screen, Colour.black, (i, len(self._board) - 2), self._board) for
                                             i in range(self.size)]

        self._board[len(self._board) - 1] = row(Colour.black, len(self._board) - 1)

    def draw(self):
        self.screen.fill(Colour.white.value)
        padding = self.screen.get_size()[0] / self.size
        self.moves = None
        for i, row in enumerate(self._board):
            for j, piece in enumerate(row):
                if i % 2 == 0 and j % 2 != 0 or i % 2 != 0 and j % 2 == 0:
                    pygame.draw.rect(self.screen, Colour.black.value,
                                     pygame.Rect(j * padding, i * padding, padding, padding))
                if piece:
                    if self._clicked == (j, i):
                        piece.draw((int(j * padding + padding // 2), int(i * padding + padding // 2)),
                                   self.size + self.size // 2, selected=True)

                        self.moves = piece.validMoves  # Saved to do later due to layering

                    else:
                        piece.draw((int(j * padding + padding // 2), int(i * padding + padding // 2)),
                                   self.size + self.size // 2)
        if self.moves:
            for move in self.moves:
                pygame.draw.circle(self.screen, Colour.blue.value,
                                   (int(move[0] * padding + padding / 2),
                                    int(move[1] * padding + padding / 2)),
                                   self.size + self.size // 2)
        if self._hovered:
            pygame.draw.rect(self.screen, Colour.red.value,
                             pygame.Rect(self._hovered[0] * padding, self._hovered[1] * padding, padding, padding), 2)

    def handleMousePos(self, pos: pygame.Vector2):
        self._hovered = (pos[0] // (self.screen.get_size()[0] / 8), pos[1] // (self.screen.get_size()[0] / 8))

    def handleMouseClick(self, pos: pygame.Vector2):
        self._clicked = (pos[0] // (self.screen.get_size()[0] / 8), pos[1] // (self.screen.get_size()[0] / 8))
