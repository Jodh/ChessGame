from typing import List, Tuple
import pygame

from Pieces.ChessPiece import ChessPiece
from Utils.Colours import Colour


class Horse(ChessPiece):
    def __init__(self, screen: pygame.Surface, colour: Colour, pos: Tuple[int, int], board: List[List[ChessPiece]]):
        super().__init__(screen, colour, pos, board)

    @property
    def validMoves(self) -> List[Tuple[int, int]]:
        moves = []

        def check(x, y):
            try:
                other = self._board[self.y + y][self.x + x]
                if other is None or other.colour != self.colour:
                    moves.append((self.x + x, self.y + y))
            except IndexError:
                pass

        check(1, 2)
        check(2, 1)
        check(-1, -2)
        check(-2, -1)
        check(1, -2)
        check(2, -1)
        check(-1, 2)
        check(-2, 1)

        return moves

    def draw(self, xy: Tuple[int, int], size: int, selected: bool = False):
        if selected:
            pygame.draw.circle(self._screen, Colour.green.value, xy, size)
        else:
            pygame.draw.circle(self._screen, self.colour.value, xy, size)
        pygame.draw.circle(self._screen, Colour.gray.value, xy, size, 4)  # Outline
