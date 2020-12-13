from typing import List, Tuple
import pygame

from Pieces.ChessPiece import ChessPiece
from Utils.Colours import Colour


class Rook(ChessPiece):
    def __init__(self, screen: pygame.Surface, colour: Colour, pos: Tuple[int, int], board: List[List[ChessPiece]]):
        super().__init__(screen, colour, pos, board)

    @property
    def validMoves(self) -> List[Tuple[int, int]]:
        moves = []

        row = [self._board[self.x][i] for i in range(len(self._board))]
        column = [self._board[i][self.y] for i in range(len(self._board))]

        i = 1
        while self.x + i < len(row) - 1:
            if row[self.x + i]:
                break
            moves.append((self.x + i, self.y))
            i += 1

        i = 1
        while self.x - i > 0:
            if row[self.x - i]:
                break
            moves.append((self.x - i, self.y))
            i += 1

        i = 1
        while self.y + i < len(column) - 1:
            if column[self.y + i]:
                break
            moves.append((self.x, self.y + i))
            i += 1

        i = 1
        while self.y - i > 0:
            if column[self.y - i]:
                break
            moves.append((self.x, self.y - i))
            i += 1

        return moves


    def draw(self, xy: Tuple[int, int], size: int, selected: bool = False):
        if selected:
            pygame.draw.circle(self._screen, Colour.green.value, xy, size)
        else:
            pygame.draw.circle(self._screen, self.colour.value, xy, size)
        pygame.draw.circle(self._screen, Colour.gray.value, xy, size, 4)  # Outline
