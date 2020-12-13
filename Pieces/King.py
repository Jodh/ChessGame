from typing import List, Tuple
import pygame

from Pieces.ChessPiece import ChessPiece
from Utils.Colours import Colour


class King(ChessPiece):
    def __init__(self, screen: pygame.Surface, colour: Colour, pos: Tuple[int, int], board: List[List[ChessPiece]]):
        super().__init__(screen, colour, pos, board)

    @property
    def validMoves(self) -> List[Tuple[int, int]]:
        raise NotImplementedError()

    def draw(self, xy: Tuple[int, int], size: int, selected: bool = False):
        if selected:
            pygame.draw.circle(self._screen, Colour.green.value, xy, size)
        else:
            pygame.draw.circle(self._screen, self.colour.value, xy, size)
        pygame.draw.circle(self._screen, Colour.gray.value, xy, size, 4)  # Outline
